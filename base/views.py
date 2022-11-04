from django.shortcuts import render
from django.http import HttpResponse
from .models import Links


""" dashboard_links =[
    {'Name':'DISD Dashboard', 'url':'https://app.powerbi.com/groups/c611ead3-2444-4578-bb8d-537e2bef1582/reports/d0704a68-55db-4430-aa31-7e4915eb6c52/ReportSectiondb7633c0122d75409c00'},
    {'Name':'T5G Website', 'url':'https://t5g.com/'},
    {'Name':'Google', 'url':'https://www.google.com/'},
    {'Name':'Stack Overflow', 'url':'https://stackoverflow.com/'},
    {'Name':'Home Page', 'url':'http://127.0.0.1:8000/'},
    {'Name':'Youtube', 'url':'https://www.youtube.com/'},
    

]  """

# Create your views here.
def home(request):
 
    return render(request,'home.html')

 

def form(request):
    dashboard_links = Links.objects.all()
    return render(request,'form.html',{'dashboard_links':dashboard_links})

def addLinks(request):
    dashboard_links = {}
    return render(request,'addLinks.html',{'dashboard_links':dashboard_links})

