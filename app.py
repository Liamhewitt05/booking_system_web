import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import json
from dataclasses import dataclass

@dataclass
class Bok:
    """klasse som holder bok navn og antall"""

    navn: str
    antall: int

def last_inn_ledige_bøker():
    """leser ledige bøker"""
    data = open("Ledige_bøker.json", "r").read()
    data = json.loads(data)
    liste = []
    for bok_navn, value in data["alle_boker"].items():
        liste.append(Bok(navn=bok_navn, antall=value["antall"]))
    return liste

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return books

def get_book(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?',
                        (book_id,)).fetchone()
    conn.close()
    return book

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    books = get_all_books()
    return render_template('index.html', books=books)



@app.route('/<int:book_id>')
def book(book_id):
    book = get_book(book_id)
    print(book)
    if book is None:
        abort(404)

    return render_template('book.html', book=book)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            post = get_book(title)
            if post is None:
                flash('Title already exists!')
            else:
                conn = get_db_connection()
                conn.execute('INSERT INTO books (title, content) VALUES (?, ?)',
                                (title, content))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    book = get_book(id)
    if book is None:
        abort(404)


    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        count = request.form['count']

        conn = get_db_connection()
        conn.execute('UPDATE books SET title = ?, summary = ?, count = ?'
                        ' WHERE id = ?',
                        (title, summary, count, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', book=book)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_book(id)
    if post is None:
        abort(404)
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))