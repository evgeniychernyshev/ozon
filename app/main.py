from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from app.ozon import create_book, add_book, search_book_by_title, search_book_by_id, remove_book_by_id, \
    create_empty_book


def main():
    app = Flask(__name__)

    container = []
    wp = create_book('War and peace', 'Tolstoy')
    anna = create_book('Anna Karenina', 'Tolstoy')

    #TODO: сделать распаковку в add_book
    container = add_book(container, wp)
    container = add_book(container, anna)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            # TODO: почистить
            results = search_book_by_title(container, search)
            return render_template('index.html', books=results, search=search)

        return render_template("index.html", books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        if book_id == 'new':
            book = create_book(title=title, author=author)
            container = add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            pass # TODO сохранить изменеия
        return redirect(url_for('book_details', book_id=book['id']))

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    app.run(port=9876, debug=True)




if __name__ == '__main__':
    main()
