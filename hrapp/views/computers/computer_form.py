import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer
from ..connection import Connection


def get_computers():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
            c.id,
            c.make,
            c.purchase_date,
            c.decommission_date
            from hrapp_computer c
        """)

        return db_cursor.fetchall()

# @login_required
def computer_form(request):
    if request.method == 'GET':
        computers = get_computers()
        template = 'computers/computers_form.html'
        context = {
            'all_computers': computers
        }

        return render(request, template, context)
        context_instance=RequestContext(request)