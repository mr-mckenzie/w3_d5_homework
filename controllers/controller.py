from app import app
from flask import render_template

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