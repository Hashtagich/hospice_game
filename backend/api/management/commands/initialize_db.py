from django.core.management.base import BaseCommand
from .command_for_npc import (
    create_categories_procedure_db, create_procedure_db, create_patient_db, create_diagnosis_db
)
from .command_for_environment import (
    create_categories_furniture_db
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

        # Environment
        create_categories_furniture_db()
        self.stdout.write(self.style.SUCCESS(
            'Initialize db Categories successfully.\nИнициализация базы данных Категорий мебели выполнена успешно.'))

        # End
        self.stdout.write(self.style.SUCCESS(
            'Initialize db command executed successfully.\nКоманда инициализации базы данных выполнена успешно.'))
