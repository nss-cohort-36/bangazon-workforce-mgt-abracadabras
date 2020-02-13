import sqlite3
# from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection


def list_departments(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department_name,
            d.budget
            e.id
        from department d
        join employee e on employee.id = u.id
        WHERE l.id = ?
        """, (department_id,))

        return db_cursor.fetchone()

def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        template = 'departments/list.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)