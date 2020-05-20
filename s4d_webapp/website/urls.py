from django.urls import path
# nieuwe view voor de advertentiepagina: list view
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    # Dit is de URL naar de home pagina.
    path('', views.home, name='web-home'),

    # Dit is de URL naar de detail pagina over de post.
    path('details/', views.details, name='web-details'),

    # Dit is de URL naar het overzicht van de posts.
    path('posts/', PostListView.as_view(), name='web-posts'),

    # Dit is de URL naar het informatie-overzicht van individuele posts.
    path('posts/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Dit is de URL naar het aanmaken van individuele posts.
    path('posts/post/new/', PostCreateView.as_view(), name='post-create'),

    # Dit is de URL naar het updaten van een post.
    path('posts/post/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),

    # Dit is de URL naar het verwijderen van een individuele posts.
    path('posts/post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),

    # Dit is de URL naar het account pagina.
    path('account/', views.account, name='web-account'),

    # Dit is de URL naar de over-ons pagina.
    path('about/', views.about, name='web-about'),
]

# browser zoekt als volgt de url:
# <app>/<model>_<viewtype>.html
