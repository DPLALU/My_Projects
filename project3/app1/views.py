from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'template/home.html')


def Employee(request):
    dict={
    'name':"laljanbaba",
    'address':"hindupur",
    'Email':"laljanbaba77gmail.com"
    }
    return render(request,'template/Employee.html',context=dict)
