from django.shortcuts import render

# Create your views here.
from app1.models import Employee
def EmployeeDetails(request):
     employee = Employee.objects.all()
     dict={'info':employee}
     return render(request,'template/details.html',dict)
