import sqlite3
from django.shortcuts import render
from hrapp.models import Employee, Department
# from django.contrib.auth.decorators import login_required
from ..connection import Connection
from .employee_details import get_employee


# Change this to departments to give user choice to choose a department
def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
            d.id,
            d.department_name
            from hrapp_department d
        """)

        all_department = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            department = Department()
            department.id = row["id"]
            department.department_name = row["department_name"]

            all_department.append(department)

        return all_department


# @login_required
def add_employee_form(request):
#     if request.method == 'GET':
        departments = get_departments()
        template = 'employees/new_employee_form.html'
        # The template expects a dictionary of data
        context = {
            'all_department': departments
        }

        return render(request, template, context)

# @login_required
def employee_edit_form(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)
        departments = get_departments()
        template = 'employees/new_employee_form.html'
        context = {
            'employee': employee,
            'all_departments': departments
        }

        return render(request, template, context)