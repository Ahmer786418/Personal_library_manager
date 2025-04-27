import json


class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()















































# import json
# import os

# data_file = 'library.txt'

# def load_library():
#     if os.path.exists(data_file):
#         with open(data_file, 'r') as file:
#             return json.load(file)
#     return []

# def save_library(library):
#     with open(data_file , 'w') as file:
#         json.dump(library,file) 

# def add_book(library):
#     title = input("Enter the title of book: ")
#     author = input("Enter the author of the book: ")
#     year = input("Enter the year of the book: ")
#     genre = input("Enter the genre of the book: ")
#     read = input("Have you read the book? (yes/no): ").lower() == 'yes'

#     new_book = {
#         'title': title,
#         'author' : author,
#         'year'  : year,
#         'genre' : genre,
#         'read'  : read
#     }

#     library.append(new_book)
#     save_library(library)
#     print(f"Book {title} added successfully. ")

# def remove_book(library):
#     title = input("Enter the title book to remove from the library")   
#     initial_length = len(library)
#     library = [book for book in library if book ['title'].lower() != title]
#     if len(library) < initial_length:
#         save_library(library)
#         print(f'Book {title} removed successfully. ')
#     else:
#         print(f"Book {title} not found in the library. ")

# def search_library(library):
#     search_by = input("Search by title or author ").lower()
#     search_term = input(f"Enter the {search_by} ").lower()

#     results = [book for book in library if search_term in book[search_by].lower()]


#     if results:
#         for book in results:
#             status = "Read" if book['read'] else "Unread"
#             print(f"{book['title']} by {book['author']} 
#                   - {book['year']} - {book['genre']} - {status}")
#     else:
#         print(f"No books found matching '{search_term}' in the {search_by} field.")

# def display_all_books(library):
#     if library:
#         for book in library:
#             status = "Read" if book['read'] else "Unread"
#             print(f"{book['title']} by {book['author']} 
#                   - {book['year']} - {book['genre']} - {status}")
#     else:
#         print("The library is empty.")


# def display_statistics(library):
#     total_books = len(library)
#     read_books = len(book for book in library if book['read'])
#     percentage_read = (read_books / total_books ) * 100 if total_books > 0 else 0

#     print(f"Total books: {total_books}")
#     print(f"Percentage read : {percentage_read:.2f}%")



# def main():
#     library = load_library()
#     while True:
#         print("menu")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search the library")
#         print("4. display all books")
#         print("5. Display statistics")
#         print("6. Exit")

#         choice =input("Enter  your choice")
#         if  choice == '1':
#             add_book(library)
#         elif choice == '2':
#             remove_book(library)
#         elif choice == '3':
#             search_library(library)
#         elif choice == '4':
#             display_all_books(library)
#         elif choice == '5':
#             display_statistics(library)
#         elif choice == '6':
#             print("Goodby !")
#             break                        
#         else:
#             print("Invaid choice. Please try again")

# if __name__ == '__main__':
#     main()            





                    















