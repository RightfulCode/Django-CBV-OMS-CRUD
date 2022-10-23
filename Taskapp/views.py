from ast import Del
from django.shortcuts import render
from .models import Employee,Role,Department
from django.views.generic import ListView, CreateView,DeleteView,UpdateView

# Create your views here.

class EmployeeListView(ListView):
    model = Employee

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/'

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = '/'