from flask import Flask, render_template, request

from app.ozon import create_book, add_book, search_book_by_title


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

    app.run(port=9876, debug=True)



if __name__ == '__main__':
    main()
