
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('add_emp', views.add_emp, name='add_emp'),
]

