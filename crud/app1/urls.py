
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('edit_employee/<int:id>', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:id>', views.delete_employee, name='delete_employee'),
]

