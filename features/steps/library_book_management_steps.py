from behave import *
from src.library_book_management import Book, Library

# SCENARIO 1: Search for a book by title and author
@given('the library contains the book "{title}" by "{author}"')
def step_given_book_exists(context, title, author):
    context.library.add_book(Book(title, author, is_available=True))


@when('I search a book "{title}" by "{author}"')
def step_when_search_title_and_author(context, title, author):
    context.search_result = context.library.search_book(title, author)


@then('I should see the book "{title}" by "{author}" in search results')
def step_then_verify_search_result(context, title, author):
    book = context.search_result
    assert book is not None, f"Book '{title}' was not found in search results."
    assert book.title == title, f"Expected title '{title}', got '{book.title}'."
    assert book.author == author, f"Expected author '{author}', got '{book.author}'."
    
 
# SCENARIO 2: Borrow a book
@when('I borrow the book "{title}"')
def step_when_borrow_book(context, title):
    context.borrow_status = context.library.borrow_book(title)


@then('The book "{title}" should be listed in my borrowed list')
def step_then_verify_borrowed_list(context, title):
    borrowed_titles = [book.title for book in context.library.borrowed_books]
    assert title in borrowed_titles, f"Book '{title}' was not found in borrowed list."
    

# SCENARIO 3: Return a book
@given('I have borrowed the book "{title}"')
def step_given_already_borrowed(context, title):
    # Setup: Create book, add to library, and mark as borrowed
    book = Book(title, "Unknown Author", is_available=False)
    context.library.add_book(book)
    context.library.borrowed_books.append(book)


@when('I return the book "{title}"')
def step_when_return_book(context, title):
    context.return_status = context.library.return_book(title)


@then('The book "{title}" should be in the availalbe list')
def step_then_verify_available(context, title):
    book = context.library.search_book(title)
    assert book is not None, f"Book '{title}' does not exist in library."
    assert book.is_available is True, f"Book '{title}' is not available."
    
    
# SCENARIO 4: Check a particular book that is borrowed
@given('Book "{title}" should be on borrowed list')
def step_given_book_on_borrowed_list(context, title):
    # Setup: Add unavailable book directly to library and borrowed list
    book = Book(title, "Unknown Author", is_available=False)
    context.library.add_book(book)
    context.library.borrowed_books.append(book)


@when('I search for the book "{title}"')
def step_when_search_by_title_only(context, title):
    context.search_result = context.library.search_book(title)


@then('It should indicate the books is not available and borrowed.')
def step_then_verify_unavailable(context):
    book = context.search_result
    assert book is not None, "Book was not found in search results."
    assert book.is_available is False, f"Expected book '{book.title}' to be borrowed, but it was available."