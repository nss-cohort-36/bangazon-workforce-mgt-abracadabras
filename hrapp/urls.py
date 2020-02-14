from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employees'),
    path('computers/', computer_list, name='computers'),
    path('computers/form', computer_form, name='computer_form'),
    path('departments/', department_list, name='departments' ),
    path('computers/<int:computer_id>/', computer_details, name='computer'),  
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('computers/<int:computer_id>/form/', computer_edit_form, name='book_edit_form')
    
]
