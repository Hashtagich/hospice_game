from environment.models import Categories, Furniture, Room
from .support_def import get_json, clear_db, create_simple_db, get_first_id


# Create
def create_categories_furniture_db():
    """Функция для наполнения базы данных Категорий мебели из файла category_furniture.json"""
    create_simple_db(name_model=Categories, name_json_file='category_furniture')


def create_room_db():
    """Функция для наполнения базы данных Комнат из файла rooms.json"""
    if not Room.objects.count():
        data = get_json(name_json_file='rooms')

        for db in data:
            Room(
                name=db['name'],
                description=db['description'],
                price=db['price'],
                is_special=db['is_special']

            ).save()


def create_furniture_db():
    """Функция для наполнения базы данных Мебели из файла furniture.json"""
    if not Furniture.objects.count():
        data = get_json(name_json_file='furniture')

        first_category = Categories.objects.first()
        first_category_id = get_first_id(first_position=first_category)

        first_room = Room.objects.first()
        first_room_id = get_first_id(first_position=first_room)

        for db in data:
            if db['room'] is None:
                Furniture(
                    name=db['name'],
                    categories=Categories(id=int(db['categories']) + first_category_id),
                    price=db['price'],
                    description=db['description']
                ).save()
            else:

                Furniture(
                    name=db['name'],
                    categories=Categories(id=int(db['categories']) + first_category_id),
                    price=db['price'],
                    room=Room(id=int(db['room']) + first_room_id),
                    description=db['description']
                ).save()


# Delete


def clear_furniture_db():
    """Функция для удаления базы данных Мебели."""
    return clear_db(name_model=Furniture)


def clear_categories_furniture_db():
    """Функция для удаления базы данных Категорий мебели."""
    return clear_db(name_model=Categories)


def clear_room_db():
    """Функция для удаления базы данных Комнат."""
    return clear_db(name_model=Room)
