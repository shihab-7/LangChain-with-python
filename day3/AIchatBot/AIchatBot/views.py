from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello world !</h1>")

def test(request):
    data={'name':"John", 'age':20}
    return render(request, 'home.html',data)