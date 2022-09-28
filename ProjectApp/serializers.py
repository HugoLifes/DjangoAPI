from rest_framework import serializers
from ProjectApp.models import Departaments, Employees

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departaments
        fields=('DepartmentId', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields=('EmployeeId', 'EmployeeName', 'Departament','DateOfJoining','PhotoFileName')