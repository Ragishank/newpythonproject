from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnSample(request):
    return HttpResponse("hello i am ragisha")
def fnTest(request):
    return render(request,'sample.html')
def fnWeb(request):
    return render(request,'web.html')

