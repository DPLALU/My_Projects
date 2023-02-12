from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,"templates/index.html")

def Indigo(request):
    dir={
    "flightNO":111,
    "flightName":"Indigo",
    "destination":"bangalore"
    }
    return render(request,"templates/indigo.html",dir)

def KingFisher(request):
    dir={
    "flightNO":222,
    "flightName":"KingFisher",
    "destination":"hyderabad"
    }
    return render(request,"templates/kingfisher.html",dir)

def AirIndia(request):
    dir={
    "flightNO":333,
    "flightName":"AirIndia",
    "destination":"mumbai"
    }
    return render(request,"templates/airindia.html",dir)
