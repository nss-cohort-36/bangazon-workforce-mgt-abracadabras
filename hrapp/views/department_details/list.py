import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection


# when we load the page, we need to get some data to show on that page (get_employees)
# when we get the data back we need to format it somehow (create_employee)
# the point of all of this is so that it is viewable on the dom for those users


# this is creating an employee from the SQL query- it's formatting the data that comes back. create employee is a factory function(it returns an object)

def create_employee(cursor,row):
    department_employees = []
    _row = sqlite3.Row(cursor,row)

    emp = Employee()
    emp.id = _row["id"]
    emp.first_name = _row["first_name"]
    emp.last_name = _row["last_name"]
    
    department_employees.append(emp)
    return department_employees 

def create_department(cursor,row):
    department = []
    _row = sqlite3.Row(cursor,row)

    dep = Department()
    dep.id = _row["id"]
    dep.department_name = _row["department_name"]
    
    department.append(dep)
    return department



# This function executes the fetch call (SQL query), it also calls create_employee function to format the rows

def get_employees(department_id):
    print(department_id)
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        # create_employee above is your function at the top, no () bc django knows to magically call it
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department_name,
            e.*
        from hrapp_department d
        left join hrapp_employee e on e.department_id = d.id
        where d.id = ?
        """, (department_id,))

        return db_cursor.fetchall()


def get_department(department_id):
    print(department_id)
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department
        # create_department above is your function at the top, no () bc django knows to magically call it
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department_name
        from hrapp_department d
        where d.id = ?
        """, (department_id,))

        return db_cursor.fetchall()






# this is calling your template and your passing the data to the template and be displayed on the DOM

def department_details(request, department_id):
    # Checking to see what kind HTTP request is being made. if it's a GET request we're telling it to execute get-employees function above
    if request.method == "GET":
        employees = get_employees(department_id)
    department = get_department(department_id)              
        # employees is a cardboard box to hold the data that get_employees is bringing back. we are passing in department_id 

    print("HELLLLLO", employees)

        
    template_name = 'department_details/list.html'

    context = {
        'department_employees': employees,
        'department': department[0][0]

    }

    return render(request, template_name, context)