# Aggregation: A relationship where one object contains references to other INDEPENDENT objects
#              "has-a" relationship

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # array of objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def main():
    library1 = Library("New York Public Library")
    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("The Hobbit", "J.R.R. Tolkein")
    library1.add_book(book1)
    library1.add_book(book2)
    print(library1.list_books())

main()

        