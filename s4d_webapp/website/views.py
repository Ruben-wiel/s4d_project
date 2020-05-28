from django.db.models import Q
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
from .models import Post, Category


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

#filter view logic handler
def is_valid_queryparam(param):
    return param != '' and param is not None

#bootstrap filter view
def bootstrap_filter_view(request):
    qs = Post.objects.all()
    categories = Category.objects.all()
    title_or_description_query = request.GET.get('title_or_description')
    publish_date = request.GET.get('publish_date')
    view_count = request.GET.get('view_count')
    category = request.GET.get('category')
    #print(title_or_author_query)

    if is_valid_queryparam(title_or_description_query):
        qs = qs.filter(Q(title__icontains=title_or_description_query) 
                        | Q(beschrijving__icontains=title_or_description_query )
                        ).distinct()

    if is_valid_queryparam(category) and category != 'Maak keuze...':
        qs = qs.filter(category__icontains=category)

    if publish_date == 'Nieuwste eerst':
        ['-date_posted']
        print("nieuwste werkt")
    elif publish_date == 'Oudste eerst':
        ['date_posted']
        print("oudste werkt ook")

    context = {
        'queryset': qs,
        'categories': categories
    }
    return render(request, 'website/bootstrap_form.html', context)


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
    fields = ['title', 'category', 'beschrijving', 'beloning']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'beschrijving', 'beloning']

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
