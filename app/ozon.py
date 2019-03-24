import uuid

def create_book(title, author):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
    }

def create_empty_book():
    return {
        'id': str(uuid.UUID()),
        'title': '',
        'author': '',
    }

def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_book_by_title(container, title):
    result = []
    for book in container:
        if book['title'] == title:
            result.append(book)
        return result

def search_book_by_id(container, id):
    for book in container:
        if book['id'] == id:
            return book

def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result



