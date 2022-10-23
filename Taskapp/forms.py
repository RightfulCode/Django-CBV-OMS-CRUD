from django import forms
from .models import Employee,Role,Department

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = '__all__'


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'