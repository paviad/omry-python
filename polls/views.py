from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = int (request.GET["a"])
    b = int (request.GET["b"])
    print("a is ", a)
    print("b is ", b)
    return HttpResponse(a+b)
