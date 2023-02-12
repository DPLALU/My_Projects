from django.shortcuts import render
from applalu.models import Mobile
# Create your views here.
def MobileDetails(request):
    mobile = Mobile.objects.all()
    dict = {"Info" : mobile}
    return render(request,"template/details.html",dict)
