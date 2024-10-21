from npc.models import Categories, Procedure, Patient, Diagnosis, Profession, Doctor
from environment.models import Room
from .support_def import get_json, clear_db, create_simple_db, get_first_id


# Create
def create_categories_procedure_db():
    """Функция для наполнения базы данных Категорий процедур из файла category_procedure.json"""
    create_simple_db(name_model=Categories, name_json_file='category_procedure')


def create_profession_db():
    """Функция для наполнения базы данных Профессий врачей из файла profession.json"""
    create_simple_db(name_model=Profession, name_json_file='profession')


def create_doctors_db():
    """Функция для наполнения базы данных Врачей из файла doctors.json"""
    if not Doctor.objects.count():
        data = get_json(name_json_file='doctors')

        first_profession = Profession.objects.first()
        first_profession_id = get_first_id(first_position=first_profession)

        first_room = Room.objects.first()
        first_room_id = get_first_id(first_position=first_room)

        for db in data:
            Doctor(
                surname=db['surname'],
                name=db['name'],
                patronymic=db['patronymic'],
                profession=Profession(id=int(db['profession']) + first_profession_id),
                work_experience=db['work_experience'],
                price=db['price'],
                room=Room(id=int(db['room']) + first_room_id),
            ).save()


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

        first_category = Categories.objects.first()
        first_category_id = get_first_id(first_position=first_category)

        first_procedure = Procedure.objects.first()
        first_procedure_id = get_first_id(first_position=first_procedure)

        for db in data:
            categories_procedure_ids = map(int, db['categories_procedure'].split())
            procedure_ids = map(int, db['procedure'].split())

            patient = Patient(
                name=db['name'],
                age=db['age'],
                diagnosis=Diagnosis(id=int(db['diagnosis']) + first_diagnosis_id)
            )

            patient.save()

            for category_id in categories_procedure_ids:
                category = Categories.objects.get(id=category_id + first_category_id)
                patient.categories_procedure.add(category)

            for procedure_id in procedure_ids:
                procedure = Procedure.objects.get(id=procedure_id + first_procedure_id)
                patient.procedure.add(procedure)


# Delete
def clear_categories_procedure_db():
    """Функция для удаления базы данных Категорий процедур."""
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


def clear_profession_db():
    """Функция для удаления базы данных Профессий врачей."""
    return clear_db(name_model=Profession)


def clear_doctor_db():
    """Функция для удаления базы данных Врачей."""
    return clear_db(name_model=Doctor)
