def create_book(title, author):
    return {
        'title': title,
        'author': author,
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


