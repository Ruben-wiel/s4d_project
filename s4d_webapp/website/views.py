from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
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
    #dit zorgt voor dat de nieuwste posts bovenaan komen te staan
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'reward']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def account(request):
    return render(request, 'website/account.html')


def about(request):
    return render(request, 'website/about.html')
