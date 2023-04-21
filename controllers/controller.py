from app import app
from flask import render_template

from models.library import books_in_library

@app.route('/library')
def index():
    return render_template('index.jinja', library_books = books_in_library)