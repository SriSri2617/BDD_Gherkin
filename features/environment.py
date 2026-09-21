from src.library_book_management import Library

def before_scenario(context, scenario):
    context.library = Library()
