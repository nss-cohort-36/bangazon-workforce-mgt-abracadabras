import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer
from ..connection import Connection


def get_computer(computer_id):
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
            WHERE c.id=?
        """,(computer_id,)) 

        return db_cursor.fetchone()

# @login_required
def computer_form(request):
    if request.method == 'GET':
        # computers = get_computers()
        template = 'computers/computers_form.html'
        context = {
            'all_computers': computers
        }

        return render(request, template, context)
        context_instance=RequestContext(request)
        
# @login_required
def computer_edit_form(request, computer_id):

    if request.method == 'GET':
        computer = get_computer(computer_id)
        # computers = get_computers()

        template = 'computers/computers_form.html'
        context = {
            'computer': computer,
            # 'all_computers': computers
        }

        return render(request, template, context)