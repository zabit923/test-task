import json
import os
from typing import List

from config import DATA_FILE
from src.models import Book


def load_data() -> List[Book]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            books_dicts = json.load(file)
            books = [Book(**book_dict) for book_dict in books_dicts]
            return books
    return []


def save_data(data: List[Book]) -> None:
    books_dicts = [book.__dict__ for book in data]
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books_dicts, file, ensure_ascii=False, indent=4)
