import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
# from libraryapp.models import model_factory
from ..connection import Connection


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        # This is different than chapter 5, because I didn't add the "conn.row_factory = model_factory(Library)" that was in chapter 3, "Advanced Creation of Simple Model Instances" section"

        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        all_libraries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            library = Library()
            library.id = row["id"]
            library.title = row["title"]
            library.address = row["address"]

            all_libraries.append(library)

        return all_libraries

@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)