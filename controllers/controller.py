from app import app
from flask import render_template, request
from models.book import Book

from models.library import books_in_library

@app.route('/library')
def index():
    return render_template('index.jinja', library_book_list = books_in_library)

@app.route('/library/<title>')
def single_book(title):

    for book in books_in_library:
        if book.title == title:
            book_to_display = book
    
    return render_template('single_book_display.jinja', single_book = book_to_display)

@app.route('/library', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']

    new_book = Book(book_title, book_author, book_genre)
    books_in_library.append(new_book)

    return render_template('index.jinja', library_book_list = books_in_library)

@app.route('/library/remove', methods=['POST'])
def remove_book():
    book_title_to_remove = request.form['title']
    print(book_title_to_remove)

    for book in books_in_library:
        if book.title == book_title_to_remove:
            books_in_library.remove(book)

    return render_template('index.jinja', library_book_list = books_in_library)