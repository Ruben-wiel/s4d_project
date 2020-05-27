from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    return render(request, 'website/home.html')


def details(request):
    return render(request, 'website/details.html', {'title': 'Details'})

# dit is de home pagina in de tutorial serie


def posts(request):
    context = {
        'adposts': Post.objects.all(),
    }
    return render(request, 'website/posts.html', context)

#bootstrap filter view
def bootstrap_filter_view(request):
    return render(request, 'website/bootstrap_form.html', {})


class PostListView(ListView):
    model = Post
    template_name = 'website/posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adposts' 
    # dit zorgt voor dat de nieuwste posts bovenaan komen te staan
    ordering = ['-date_posted']
    # paginate_by zorgt ervoor dat niet alle posts/advertenties op 1 pagina te zien zijn.
    paginate_by = 5


#Laat alle posts zien van een gebruiker op zijn profiel
class UserPostListView(ListView):
    model = Post
    template_name = 'website/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adposts'
    # paginate_by zorgt ervoor dat niet alle posts/advertenties op 1 pagina te zien zijn.
    paginate_by = 5

    #Laat een 404 pagina zien i.p.v. een lege pagina als functie niet mogelijk is. 
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titel', 'beschrijving', 'beloning']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titel', 'beschrijving', 'beloning']

    # de auteur wordt gelijk gezet aan de gene die dan ingelogd is, voordat de .form_valid method start.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # met deze functie test de app of de de user wel bij de post hoort voor het aanpassen
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def account(request):
    return render(request, 'website/account.html')


def about(request):
    return render(request, 'website/about.html')
