class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available        


class Library:
    def __init__(self):
        self.books = []                 # List to store all Book instances present in the library database
        self.borrowed_books = []        # List to keep track of books that have been borrowed by users
    
    def add_book(self, book: Book):
        self.books.append(book)

    def search_book(self, title: str, author: str = None) -> Book | None:
         #Searches for a book by title and optionally by author.
       for book in self.books:
           # First, check if the title matches
           if book.title == title:
               # If no author was specified (author is None), OR if the author matches:
               if author is None or book.author == author:
                   return book                              # Return the Book object
       return None                                          # Return None if no matching book was found after checking all items

    def borrow_book(self, title: str) -> bool:
         # Borrows a book by title if it is available.
        book = self.search_book(title)           # Find the book using our search method
         # Ensure the book exists AND is currently available for borrowing
        if book and book.is_available:
            book.is_available = False                         # Book unavailable
            self.borrowed_books.append(book)                  # Add to borrowed list
            return True
        return False

    def return_book(self, title: str) -> bool:
        # Returns a previously borrowed book back to the library.
        for book in self.borrowed_books:                      # Search through the list of currently borrowed books
            if book.title == title:
                book.is_available = True                      # Book status back to available
                self.borrowed_books.remove(book)              # Remove from borrowed list
                return True
        return False
        