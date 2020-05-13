from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'website/home.html')


def details(request):
    return render(request, 'website/details.html', {'title': 'Details'})


def posts(request):
    context = {
        'adposts': Post.objects.all()
    }
    return render(request, 'website/posts.html', context)


def account(request):
    return render(request, 'website/account.html')


def about(request):
    return render(request, 'website/about.html')
