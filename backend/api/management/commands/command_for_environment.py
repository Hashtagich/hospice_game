from environment.models import Categories
from .support_def import get_json, clear_db, create_simple_db


# Create
def create_categories_furniture_db():
    """Функция для наполнения базы данных Категорий мебели из файла category_furniture.json"""
    create_simple_db(name_model=Categories, name_json_file='category_furniture')


# Delete
def clear_categories_furniture_db():
    """Функция для удаления базы данных Категорий мебели."""
    return clear_db(name_model=Categories)
