from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView

)
from .models import Post, Category
from users.models import Location, UserProfile
from django.core.paginator import Paginator


def home(request):
    return render(request, 'website/home.html')


def details(request):
    return render(request, 'website/details.html', {'title': 'Details'})


def posts(request):
    context = {
        'adposts': Post.objects.all(),
    }
    return render(request, 'website/posts.html', context)


def howto(request):
    return render(request, 'website/howto.html')

# filter view logic handler


def is_valid_queryparam(param):
    return param != '' and param is not None


class PostListView(ListView):
    template_name = 'website/posts.html'
    context_object_name = 'adposts'
    ordering = ['-date_posted']
    paginate_by = 5
    model = Post
    #post.author.userprofile.locatie

    def get(self, request):
        qs = Post.objects.all().order_by('-date_posted')
        #qs2 = UserProfile.objects.all().order_by('-date_posted')

        title_or_description_query = request.GET.get('title_or_description')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')
        category = request.GET.get('category')
        location = request.GET.get('location')


        paginator = Paginator(qs, 5)
        page = request.GET.get('page')
        rendering = paginator.get_page(page)
        categories = Category.objects.all().order_by('-date_posted')
        locations = Location.objects.all().order_by('-date_posted')

        paginator2 = Paginator(categories, 5)
        paginator3 = Paginator(locations, 5)

        page2 = request.GET.get('page')
        rendering2 = paginator2.get_page(category)
        rendering3 = paginator3.get_page(location)


        ordering = ['-date_posted']
        if is_valid_queryparam(title_or_description_query):
            qs = qs.filter(Q(titel__icontains=title_or_description_query)
                           | Q(beschrijving__icontains=title_or_description_query)
                           ).distinct()
            paginator = Paginator(qs, 5)
            page = request.GET.get('page')
            rendering = paginator.get_page(page)

        if is_valid_queryparam(category) and category != 'Maak keuze...':
            qs = qs.filter(categorie__icontains=category)
            paginator = Paginator(qs, 5)
            page = request.GET.get('page')
            rendering = paginator.get_page(page)

        if is_valid_queryparam(date_min):
            qs = qs.filter(date_posted__gte=date_min)
            paginator = Paginator(qs, 5)
            page = request.GET.get('page')
            rendering = paginator.get_page(page)

        if is_valid_queryparam(date_max):
            qs = qs.filter(date_posted__lt=date_max)
            paginator = Paginator(qs, 5)
            page = request.GET.get('page')
            rendering = paginator.get_page(page)

        if is_valid_queryparam(location) and location != 'Maak keuze...':
            qs = qs.filter(locatie__icontains=location)
            print("testing")
            paginator3 = Paginator(qs, 5)
            page = request.GET.get('page')
            rendering3 = paginator3.get_page(page)

        context = {
            'queryset': rendering,
            'categories': rendering2,
            'location': rendering3,
        }

        Post.objects.order_by('-date_posted')
        return render(request, 'website/posts.html', context)

# Laat alle posts zien van een gebruiker op zijn profiel


class UserPostListView(ListView):
    model = Post
    template_name = 'website/user_posts.html'
    context_object_name = 'adposts'
    paginate_by = 5

    # Laat een 404 pagina zien i.p.v. een lege pagina als functie niet mogelijk is.
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titel', 'categorie', 'beschrijving', 'beloning']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titel', 'categorie', 'beschrijving', 'beloning']

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


def about(request):
    return render(request, 'website/about.html')
