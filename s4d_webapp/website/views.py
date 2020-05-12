from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Pagina</h1>')

def about(request):
    return HttpResponse('<h1>Over Ons</h1>')

def posts(request):
    return HttpResponse('<h1>Advertenties</h1>')

def account(request):
    return HttpResponse('<h1>User Portal</h1>')
