from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    return render(request, 'website/home.html')


def details(request):
    return render(request, 'website/details.html', {'title': 'Details'})

#dit is de home pagina in de tutorial serie
def posts(request):
    context = {
        'adposts': Post.objects.all()
    }
    return render(request, 'website/posts.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'website/posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'adposts'
    ordering = ['-date_posted']

def account(request):
    return render(request, 'website/account.html')


def about(request):
    return render(request, 'website/about.html')
