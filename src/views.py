from typing import List

from src.models import Book
from src.utils import generate_id, save_data, print_book


def add_book(data: List[Book]) -> None:
    title = input("Введите название книги: ").strip()

    if any(book.title.lower() == title.lower() for book in data):
        print("\n⚠ Ошибка: Книга с таким названием уже существует.\n")
        return

    author = input("Введите автора книги: ").strip()
    year_input = input("Введите год издания книги: ").strip()

    if not year_input.isdigit():
        print("\n⚠ Ошибка: год издания должен быть числом.\n")
        return

    year = int(year_input)
    new_id = generate_id(data)
    new_book = Book(id=new_id, title=title, author=author, year=year)
    data.append(new_book)
    save_data(data)
    print("\n✅ Книга успешно добавлена!\n")


def delete_book(data: List[Book]) -> None:
    try:
        book_id = int(input("Введите ID книги для удаления: ").strip())
        book_to_remove = next((book for book in data if book.id == book_id), None)
        if book_to_remove:
            data.remove(book_to_remove)
            save_data(data)
            print("\n✅ Книга успешно удалена!\n")
        else:
            print("\n⚠ Ошибка: книга с таким ID не найдена.\n")
    except ValueError:
        print("\n⚠ Ошибка: ID должен быть числом.\n")


def search_book(data: List[Book]) -> None:
    criteria = input("Введите критерий поиска (title, author, year): ").strip().lower()
    query = input("Введите значение для поиска: ").strip()

    if criteria == "year" and not query.isdigit():
        print("\n⚠ Ошибка: год должен быть числом.\n")
        return

    results = [
        book for book in data
        if (criteria == "title" and book.title.lower() == query.lower())
        or (criteria == "author" and book.author.lower() == query.lower())
        or (criteria == "year" and str(book.year) == query)
    ]

    if results:
        print("\n🔍 Найденные книги:")
        print("=" * 60)
        for book in results:
            print_book(book)
        print("=" * 60)
    else:
        print("\n⚠ Книги не найдены.\n")


def change_status(data: List[Book]) -> None:
    try:
        book_id = int(input("Введите ID книги для изменения статуса: ").strip())
        new_status = input("Введите новый статус (в наличии, выдана): ").strip()
        if new_status not in ["в наличии", "выдана"]:
            print("\n⚠ Ошибка: статус может быть только 'в наличии' или 'выдана'.\n")
            return
        book_to_update = next((book for book in data if book.id == book_id), None)
        if book_to_update:
            book_to_update.status = new_status
            save_data(data)
            print("\n✅ Статус книги успешно изменен!\n")
        else:
            print("\n⚠ Ошибка: книга с таким ID не найдена.\n")
    except ValueError:
        print("\n⚠ Ошибка: ID должен быть числом.\n")


def display_books(data: List[Book]) -> None:
    if data:
        print("\n📚 Список книг:")
        print("=" * 60)
        for book in data:
            print_book(book)
        print("=" * 60)
    else:
        print("\n⚠ Библиотека пуста.\n")
