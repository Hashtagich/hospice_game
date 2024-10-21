from django.core.management.base import BaseCommand
from .command_for_npc import (
    create_categories_procedure_db, create_procedure_db, create_patient_db, create_diagnosis_db, create_profession_db,
    create_doctors_db
)
from .command_for_environment import (
    create_categories_furniture_db, create_room_db, create_furniture_db
)


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать баз данных'''

    def handle(self, *args, **options):
        # NPC
        create_categories_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Categories successfully.\nИнициализация базы данных Категорий процедур выполнена успешно.'))

        create_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Procedure successfully.\nИнициализация базы данных Процедур выполнена успешно.'))

        create_diagnosis_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Diagnosis successfully.\nИнициализация базы данных Диагнозы выполнена успешно.'))

        create_patient_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Patient successfully.\nИнициализация базы данных Пациентов выполнена успешно.'))

        create_profession_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Profession successfully.\nИнициализация базы данных Профессий врачей выполнена успешно.'))

        # Environment
        create_room_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Rooms successfully.\nИнициализация базы данных Комнат выполнена успешно.'))

        create_categories_furniture_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Categories successfully.\nИнициализация базы данных Категорий мебели выполнена успешно.'))

        create_furniture_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Furniture successfully.\nИнициализация базы данных Мебели выполнена успешно.'))

        create_doctors_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Doctors successfully.\nИнициализация базы данных Врачей выполнена успешно.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
