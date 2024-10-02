from django.core.management.base import BaseCommand
from .command_for_npc import (
    create_categories_db, create_procedure_db, create_patient_db, create_diagnosis_db)


class Command(BaseCommand):
    """
    Класс для инициализации баз данных. Каждая база данных создаётся через запуск конкретной функции.
    Подробное описание какая база создаётся и как описано непосредственно в функциях.
    """
    help = '''
    Initialize db 
    Инициализировать баз данных'''

    def handle(self, *args, **options):
        create_categories_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Categories successfully.\nИнициализация базы данных Категории выполнена успешно.'))

        create_procedure_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Procedure successfully.\nИнициализация базы данных Процедур выполнена успешно.'))

        create_diagnosis_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Diagnosis successfully.\nИнициализация базы данных Диагнозы выполнена успешно.'))

        create_patient_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Patient successfully.\nИнициализация базы данных Пациентов выполнена успешно.'))

        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
