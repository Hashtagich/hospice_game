import re
from django.core.exceptions import ValidationError


class UppercaseValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну заглавную латинскую букву.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну заглавную латинскую букву."


class LowercaseValidator:
    def validate(self, password, user=None):
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну строчную латинскую букву.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну строчную латинскую букву."


class NumericPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'[0-9]', password):
            raise ValidationError(
                "Пароль должен содержать хотя бы одну цифру.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return "Ваш пароль должен содержать хотя бы одну цифру."
