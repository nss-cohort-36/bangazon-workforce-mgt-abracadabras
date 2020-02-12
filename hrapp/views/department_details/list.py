import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection


def department_details(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    
        db_cursor.execute("""
        select
            d.id,
            d.department_name,
            e.*
        from department d
        join employee e on d.id = e.department
        """)

        all_departments = []
        dataset = db_cursor.fetchall()

    #     for row in dataset:
    #         lib = Librarian()
    #         lib.id = row["id"]
    #         lib.location_id = row["location_id"]
    #         lib.user_id = row["user_id"]
    #         lib.first_name = row["first_name"]
    #         lib.last_name = row["last_name"]
    #         lib.email = row["email"]

    #         all_librarians.append(lib)

    # template_name = 'librarians/list.html'

    # context = {
    #     'all_librarians': all_librarians
    # }

    # return render(request, template_name, context)