[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://forthebadge.com)

## Quick Start

1) Install python3.11
2) git clone https://github.com/zabit923/test-task.git
3) ``` pip install pre-commit ```
4) Install pre-commit hooks:  ```$ pre-commit install```
5) ``` python app.py ```

## `Project Styling` ✅

| Tools          |                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                       |
| -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `isort`        |                                                                                                                                                                                                         isort your python imports for you so you don't have to. isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections.                                                                                                                                                                                                         |
| `black`        |                       Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters. Blackened code looks the same regardless of the project you're reading. Formatting becomes transparent after a while and you can focus on the content instead. Black makes code review faster by producing the smallest diffs possible.                       |
| `pre-commit`   | Git hooks allow you to run scripts any time you want to commit or push. This lets us run all of our linting and tests automatically every time we commit/push. Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks. |

For more information on `Project Styling` check out the detailed guide 👉 [How to set up a perfect Python project](https://sourcery.ai/blog/python-best-practices/)

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

