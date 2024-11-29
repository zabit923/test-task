[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

## Quick Start

1) Install python3.11
2) git clone https://github.com/zabit923/test-task.git
3) ``` python app.py ```

## Functionalities

### 1. Add a Book
- Prompts the user to enter the title, author, and year of publication.
- Generates a unique ID for the new book.
- Adds the book to the library with the status `"available"`.
- Ensures the book title is unique before adding it to the library.

### 2. Delete a Book
- Prompts the user to enter the ID of the book to delete.
- Removes the book from the library if the ID exists.
- Displays a message confirming successful deletion or an error if the book is not found.

### 3. Search for a Book
- Allows the user to search for a book by one of the following criteria:
  - **Title**
  - **Author**
  - **Year of Publication**
- The search is case-insensitive and matches the exact value provided by the user.
- Displays a list of matching books or a message if no books are found.

### 4. Display All Books
- Displays a list of all books currently in the library with the following details:
  - ID
  - Title
  - Author
  - Year of Publication
  - Status (either "available" or "borrowed")

### 5. Change Book Status
- Prompts the user to enter the ID of the book to modify the status.
- The user can set the status to either `"available"` or `"borrowed"`.
- If the ID is valid, the status is updated, and the changes are saved.

## Data Storage
- All book data is saved in a **JSON file** (`data.json`), ensuring persistence across application runs.

