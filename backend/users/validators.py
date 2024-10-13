from re import match, search
from django.core.exceptions import ValidationError


class UppercaseValidator:
    def validate(self, password, user=None):
        if not search(r'[A-Z]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну заглавную латинскую букву.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну заглавную латинскую букву."


class LowercaseValidator:
    def validate(self, password, user=None):
        if not search(r'[a-z]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну строчную латинскую букву.",
                code='password_no_lower',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну строчную латинскую букву."


class NumericPasswordValidator:
    def validate(self, password, user=None):
        if not search(r'[0-9]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну цифру.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну цифру."


def _validate_username(username):
    """Проверка username."""
    if not (4 <= len(username) <= 15):
        raise ValidationError("Username должен быть от 4 до 15 символов.")

    if not search(r'[a-z]', username):
        raise ValidationError(
            "Username должен содержать хотя бы одну строчную латинскую букву."
        )

    if not search(r'[A-Z]', username):
        raise ValidationError(
            "Username должен содержать хотя бы одну заглавную латинскую букву."
        )

    if match("^\d+$", username):
        raise ValidationError("Username не должен содержать только цифры.")

    if not match("[a-zA-Zа-яА-ЯёЁ]*$", username):
        raise ValidationError("Username не может состоять только из цифр и спец символов.")
