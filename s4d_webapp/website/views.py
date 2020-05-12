from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def posts(request):
    return render(request, 'website/posts.html')

def account(request):
    return render(request, 'website/account.html')
