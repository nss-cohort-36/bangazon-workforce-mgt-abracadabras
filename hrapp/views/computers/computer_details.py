import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer
from hrapp.models import model_factory
from ..connection import Connection


def computer_list(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
           c.id,
           c.make,
           c.purchase_date,
           c.decommission_date
        FROM hrapp_computer c
        WHEREc.id = ?
        """, (computer_id,))

        return db_cursor.fetchone()

@login_required
def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)

        template = 'computers/detail.html'
        context = {
            'computer': computer
        }

        return render(request, template, context)