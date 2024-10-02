from npc.models import Categories, Procedure, Patient, Diagnosis
from .support_def import get_json, clear_db, create_simple_db, get_first_id


# Create
def create_categories_db():
    """Функция для наполнения базы данных Категории из файла category.json"""
    create_simple_db(name_model=Categories, name_json_file='category')


def create_procedure_db():
    """Функция для наполнения базы данных Процедур из файла procedure.json"""
    if not Procedure.objects.count():
        data = get_json(name_json_file='procedure')

        first_category = Categories.objects.first()
        first_category_id = get_first_id(first_position=first_category)

        for db in data:
            Procedure(
                name=db['name'],
                description=db['description'],
                categories=Categories(id=int(db['categories']) + first_category_id),
                effectiveness=db['effectiveness'],
                execution_time=db['execution_time'],
            ).save()


def create_diagnosis_db():
    """Функция для наполнения базы данных Диагноза из файла diagnosis.json"""
    if not Diagnosis.objects.count():
        data = get_json(name_json_file='diagnosis')

        for db in data:
            Diagnosis(
                name=db['name'],
                symptoms=db['symptoms'],
            ).save()


def create_patient_db():
    """Функция для наполнения базы данных Пациента из файла patient.json"""
    if not Patient.objects.count():
        data = get_json(name_json_file='patient')

        first_diagnosis = Diagnosis.objects.first()
        first_diagnosis_id = get_first_id(first_position=first_diagnosis)

        for db in data:
            Patient(
                name=db['name'],
                age=db['age'],
                diagnosis=Diagnosis(id=int(db['diagnosis']) + first_diagnosis_id)
            ).save()


# Delete
def clear_categories_db():
    """Функция для удаления базы данных Категории."""
    return clear_db(name_model=Categories)


def clear_procedure_db():
    """Функция для удаления базы данных Процедур."""
    return clear_db(name_model=Procedure)


def clear_diagnosis_db():
    """Функция для удаления базы данных Диагнозов."""
    return clear_db(name_model=Diagnosis)


def clear_patient_db():
    """Функция для удаления базы данных Пациентов."""
    return clear_db(name_model=Patient)
