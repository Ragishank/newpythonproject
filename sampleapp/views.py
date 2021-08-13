from django.shortcuts import render
from django.http import HttpResponse
from . models import student
# Create your views here.
# def fnSample(request):
#     return HttpResponse("hello i am ragisha")
def fnSample(request):
    return render(request,'sample.html')
def fnAdminMaster(request):
    return render(request,'adminmaster.html')
def fnHome(request):
    return render(request,'home.html')
def fnMaster(request):
    return render(request,'samplemaster.html')
def fnTest(request):
    return render(request,"test.html")

def fnapp1(request):
    return HttpResponse("hi i am Ragisha")
    
def fncrud(request):
    if request.method=='POST':
        fname=request.POST['fname']
        contact=request.POST['contact']
        dob=request.POST['dob']
        studObj=student(firstname=fname,contact=contact,dob=dob)
        studObj.save()
    return render(request,'crud.html')  
