from typing import List

from src.models import Book


def generate_id(data: List[Book]) -> int:
    max_id = max((book.id for book in data), default=0)
    return max_id + 1


def print_book(book: Book) -> None:
    print(f"ID: {book.id:<5} | Название: {book.title:<20} | Автор: {book.author:<15} | "
          f"Год: {book.year:<5} | Статус: {book.status}")
