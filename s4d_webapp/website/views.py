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
#paginator voor het filter systeem
from django.core.paginator import Paginator


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

def instructions(request):
    return render(request, 'website/instructions.html')

#filter view logic handler
def is_valid_queryparam(param):
    return param != '' and param is not None

class PostListView(ListView):
    template_name = 'website/posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adposts' 
    # dit zorgt voor dat de nieuwste posts bovenaan komen te staan
    ordering = ['-date_posted']
    # paginate_by zorgt ervoor dat niet alle posts/advertenties op 1 pagina te zien zijn.
    paginate_by = 5
    model = Post
    def get(self, request):
        #stap 1 voor paginator:
        qs = Post.objects.all().order_by('-date_posted')
        #stap 2 voor paginator:
        paginator = Paginator(qs, 5) # Show 5 posts per page
        #stap 3 voor paginator:
        page = request.GET.get('page')
        #stap 4 voor paginator:
        rendering = paginator.get_page(page)

######################################################################################3

        #stap 1 voor paginator2:
        categories = Category.objects.all().order_by('-date_posted')
        #stap 2 voor paginator2:
        paginator2 = Paginator(categories, 5) # Show 5 categories per page
        #stap 3 voor paginator:
        page2 = request.GET.get('page')
        #stap 4 voor paginator:
        #rendering2 = paginator2.get_page(category)

        #gebruik dit voor de template
        title_or_description_query = request.GET.get('title_or_description')
        date_min = request.GET.get('date_min') 
        date_max = request.GET.get('date_max')
        category = request.GET.get('category')
        #stap 4 voor paginator:
        rendering2 = paginator2.get_page(category)
        
        ordering = ['-date_posted']
        if is_valid_queryparam(title_or_description_query):
            qs = qs.filter(Q(title__icontains=title_or_description_query) 
                            | Q(beschrijving__icontains=title_or_description_query )
                            ).distinct()
            paginator = Paginator(qs, 5) # Show 5 posts per page
            #stap 3 voor paginator:
            page = request.GET.get('page')
            #stap 4 voor paginator:
            rendering = paginator.get_page(page)
        if is_valid_queryparam(category) and category != 'Maak keuze...':
            qs = qs.filter(category__icontains=category)
            paginator = Paginator(qs, 5) # Show 5 posts per page
            #stap 3 voor paginator:
            page = request.GET.get('page')
            #stap 4 voor paginator:
            rendering = paginator.get_page(page)
        if is_valid_queryparam(date_min):
            qs = qs.filter(date_posted__gte=date_min)
            paginator = Paginator(qs, 5) # Show 5 posts per page
            #stap 3 voor paginator:
            page = request.GET.get('page')
            #stap 4 voor paginator:
            rendering = paginator.get_page(page)
        if is_valid_queryparam(date_max):
            qs = qs.filter(date_posted__lt=date_max )
            paginator = Paginator(qs, 5) # Show 5 posts per page
            #stap 3 voor paginator:
            page = request.GET.get('page')
            #stap 4 voor paginator:
            rendering = paginator.get_page(page)  
        
        context = {
            'queryset': rendering,
            'categories': rendering2,
        }

        Post.objects.order_by('-date_posted')
        return render(request, 'website/posts.html', context)

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


############################# favourite class #######################
class Favourite():
    is_favourite = False
#####################################################################

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

def favourite(request):
    is_favourite = False
    return render(request, 'website/posts.html')