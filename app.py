from src.utils import load_data
from src.views import (
    add_book,
    delete_book,
    search_book,
    display_books,
    change_status
)


def main() -> None:
    data = load_data()
    while True:
        print("\nМеню:")
        print("=" * 25)
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        print("=" * 25)

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_book(data)
        elif choice == "2":
            delete_book(data)
        elif choice == "3":
            search_book(data)
        elif choice == "4":
            display_books(data)
        elif choice == "5":
            change_status(data)
        elif choice == "6":
            print("\n👋 До свидания!\n")
            break
        else:
            print("\n⚠ Ошибка: неверный выбор.\n")


if __name__ == "__main__":
    main()
