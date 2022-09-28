from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from rest_framework import parsers
from django.http import response

from ProjectApp.models import Departaments, Employees
from ProjectApp.serializers import DepartamentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method== 'GET':
        department = Departaments.objects.all()
        department_serializer = DepartamentSerializer(department, many=True)
        return response.JsonResponse(department_serializer.data,safe=False)
    elif request.method== 'POST':
        department_data = parsers.JSONParser().parse(request)
        department_serializer= DepartamentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return response.JsonResponse('Added Successfully', safe= False)
        return response.JsonResponse('Failed to add')
    elif request.method == 'PUT':
        department_data= parsers.JSONParser().parse(request)
        print(department_data['DepartmentId'])
        department =  Departaments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartamentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return response.JsonResponse("Update Successfully", safe=False)
        return response.JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department = Departaments.objects.get(DepartmentId=id)
        department.delete()
        return response.JsonResponse("Deleted Successfully", safe= False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method== 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return response.JsonResponse(employees_serializer.data,safe=False)
    elif request.method== 'POST':
        employee_data = parsers.JSONParser().parse(request)
        employees_serializer= EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return response.JsonResponse('Added Successfully', safe= False)
        return response.JsonResponse('Failed to add')
    elif request.method == 'PUT':
        employee_data= parsers.JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employees,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return response.JsonResponse("Update Successfully", safe=False)
        return response.JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeeId=id)
        employees.delete()
        return response.JsonResponse("Deleted Successfully", safe= False)

@csrf_exempt
def saveFile(request):
    file= request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return response.JsonResponse(file_name, safe=False)

