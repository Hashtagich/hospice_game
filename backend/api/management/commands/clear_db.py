from django.core.management.base import BaseCommand
from .command_for_npc import (
    clear_categories_procedure_db, clear_procedure_db, clear_patient_db, clear_diagnosis_db, clear_profession_db,
    clear_doctor_db
)

from .command_for_environment import (
    clear_categories_furniture_db, clear_furniture_db, clear_room_db
)


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать базы данных'''

    def handle(self, *args, **options):
        # NPC
        count = clear_categories_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Категорий процедур в количестве {count} шт. удалены из базы данных.'))

        count = clear_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Процедур в количестве {count} шт. удалены из базы данных.'))

        count = clear_diagnosis_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Диагнозов в количестве {count} шт. удалены из базы данных.'))

        count = clear_patient_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Пациентов в количестве {count} шт. удалены из базы данных.'))

        # Environment
        count = clear_furniture_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Мебели в количестве {count} шт. удалены из базы данных.'))

        count = clear_categories_furniture_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Категорий мебели в количестве {count} шт. удалены из базы данных.'))

        count = clear_doctor_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Врачей в количестве {count} шт. удалены из базы данных.'))
        count = clear_room_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Комнат в количестве {count} шт. удалены из базы данных.'))

        count = clear_profession_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Профессий врачей в количестве {count} шт. удалены из базы данных.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
