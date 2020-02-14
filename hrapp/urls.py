from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('computers/', computer_list, name='computer_list'),
    path('department/details/<int:department_id>/', department_details, name='department_details'),
    path('computers/form', computer_form, name='computer_form'),
    path('employees/form', add_employee_form, name='employees_form'),
    path('departments/', department_list, name='departments' ),
    path('computers/<int:computer_id>/', computer_details, name='computer'),
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('computers/<int:computer_id>/form/', computer_edit_form, name='computer_edit_form')
    
]
