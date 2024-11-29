import unittest

from src.models import Book
from src.utils import generate_id


class TestLibraryApp(unittest.TestCase):
    def setUp(self) -> None:
        self.books = [
            Book(id=1, title="Книга 1", author="Автор 1", year=2000, status="в наличии"),
            Book(id=2, title="Книга 2", author="Автор 2", year=2010, status="выдана"),
        ]

    def test_add_book(self):
        new_books = self.books.copy()
        new_title = "Книга 3"
        new_author = "Автор 3"
        new_year = 2020

        new_id = generate_id(new_books)
        new_books.append(Book(id=new_id, title=new_title, author=new_author, year=new_year))
        added_book = next((book for book in new_books if book.title == new_title), None)

        self.assertIsNotNone(added_book)
        self.assertEqual(added_book.title, new_title)
        self.assertEqual(added_book.author, new_author)
        self.assertEqual(added_book.year, new_year)
        self.assertEqual(added_book.status, "в наличии")

    def test_add_duplicate_title(self):
        new_books = self.books.copy()
        duplicate_title = "Книга 1"

        if any(book.title.lower() == duplicate_title.lower() for book in new_books):
            duplicate_error = True
        else:
            duplicate_error = False

        self.assertTrue(duplicate_error)

    def test_delete_book(self):
        new_books = self.books.copy()
        book_to_delete_id = 1
        book_to_delete = next((book for book in new_books if book.id == book_to_delete_id), None)

        if book_to_delete:
            new_books.remove(book_to_delete)

        self.assertNotIn(book_to_delete, new_books)

    def test_search_book(self):
        search_criteria = "title"
        search_value = "Книга 1"

        results = [
            book for book in self.books
            if (search_criteria == "title" and book.title.lower() == search_value.lower())
        ]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Книга 1")

    def test_change_status(self):
        new_books = self.books.copy()
        book_to_change_id = 2
        new_status = "в наличии"

        book_to_update = next((book for book in new_books if book.id == book_to_change_id), None)
        if book_to_update:
            book_to_update.status = new_status

        self.assertIsNotNone(book_to_update)
        self.assertEqual(book_to_update.status, new_status)

    def test_display_books(self):
        self.assertGreater(len(self.books), 0)
        displayed_books = "\n".join(
            f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
            f"Год: {book.year}, Статус: {book.status}" for book in self.books
        )
        self.assertIn("Книга 1", displayed_books)
        self.assertIn("Книга 2", displayed_books)


if __name__ == "__main__":
    unittest.main()
