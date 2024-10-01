from django.core.management.base import BaseCommand
from .command_for_npc import (
    clear_categories_db, clear_procedure_db, clear_patient_db)


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать базы данных'''

    def handle(self, *args, **options):
        count = clear_categories_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Категорий в количестве {count} шт. удалены из базы данных.'))

        count = clear_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            f'{count} records deleted from the database.\nЗаписи Процедур подписчиков в количестве {count} шт. удалены из базы данных.'))

        # count = clear_patient_db()
        # self.stdout.write(self.style.SUCCESS(
        #     f'{count} records deleted from the database.\nЗаписи Пациентов подписчиков в количестве {count} шт. удалены из базы данных.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))