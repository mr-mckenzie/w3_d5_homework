from app import app
from flask import render_template, request
from models.book import Book

from models.library import books_in_library

@app.route('/library')
def index():
    return render_template('index.jinja', library_book_list = books_in_library)

@app.route('/library/<title>')
def individual_book(title):
    chosen_book = []
    for book in books_in_library:
        if book.title == title:
            chosen_book.append(book)
    
    return render_template('index.jinja', library_book_list = chosen_book)

@app.route('/library', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']

    new_book = Book(book_title, book_author, book_genre)
    books_in_library.append(new_book)

    return render_template('index.jinja', library_book_list = books_in_library)