from django.shortcuts import render
from app1.models import Employee
from app1.form import Forms1
# Create your views here.
def index(request):
    return render(request,"template/index.html")

def models(request):
    data = Employee.objects.all()
    dict = {"information":data}
    return render(request,"template/info.html",dict)

def forms1(request):
    data2 = Forms1()
    if request.method == 'POST':
      data3 = Forms1(request.POST)
      if data3.is_valid():
          data3.save()
      return index(request)
    return render(request,'template/info1.html',{'info':data2})
