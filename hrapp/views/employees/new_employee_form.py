import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from libraryapp.models import Book
# from libraryapp.models import Library
# from libraryapp.models import model_factory
from ..connection import Connection


def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            emp.id,
            emp.first_name,
            emp.last_name,
            emp.start_date,
            emp.is_supervisor,
            emp.department_id
        from hrapp_employee emp
        """)

        all_employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee()
            employee.id = row["id"]
            employee.first_name = row["first_name"]
            employee.last_name = row["last_name"]
            employee.start_date = row["start_date"]
            employee.is_supervisor = row["is_supervisor"]
            employee.department_id = row["department_id"]

            all_employees.append(employee)

        return all_employees


# @login_required
# def add_employee_form(request):
#     if request.method == 'GET':
#         libraries = get_libraries()
#         template = 'books/form.html'
#         context = {
#             'all_libraries': libraries
#         }

#         return render(request, template, context)