import json
import os

if os.path.exists("library.txt"):
    with open("library.txt", "r") as file:
        library = json.load(file)
else:
    library = []

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    save_library()
    print(" Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    global library
    original_count = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]
    if len(library) < original_count:
        save_library()
        print(" Book removed successfully!")
    else:
        print(" Book not found.")

def search_books():
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice (1 or 2): ")
    if choice == "1":
        term = input("Enter the title: ").lower()
        results = [book for book in library if term in book["title"].lower()]
    elif choice == "2":
        term = input("Enter the author: ").lower()
        results = [book for book in library if term in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books():
    if not library:
        print("No books in the library.")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics():
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total) * 100
    print(f"\n Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

def main():
    while True:
        print("\n Welcome to My Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved to file. Thanks!")
            break
        else:
            print("Invalid choice.Try again.")

if __name__ == "__main__":
    main()
