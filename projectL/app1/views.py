from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function(request):
    return HttpResponse("<h1>this is basic level project</h1>")
