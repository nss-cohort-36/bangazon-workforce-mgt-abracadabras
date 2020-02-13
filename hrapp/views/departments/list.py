import sqlite3
# from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from ..connection import Connection


def list_departments(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department_name,
            d.budget,
            e.first_name,
        from department d
        join employee e on e.department_id = d.id
        """)

        all_departments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            department = Department()
            department.id = row["id"]
            department.name = row["department_name"]
            department.budget = row["budget"]
            department.employee_name = row["first_name"]

            all_departments.append(department)

    template_name = 'departments/list.html'

    context = {
        'all_departments': all_departments
    }

    return render(request, template_name, context)