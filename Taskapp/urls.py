from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view()),
    path('create/', views.EmployeeCreate.as_view(), name='Create'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='Delete'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='Update'),
]