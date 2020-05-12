from django.urls import path
from . import views

urlpatterns = [
    #Dit is de URL naar de home pagina.
    path('', views.home, name='web-home'),

    #Dit is de URL naar de detail pagina over de post.
    path('details/', views.details, name='web-details'),

    #Dit is de URL naar het overzicht van de posts.
    path('posts/', views.posts, name='web-posts'),

    #Dit is de URL naar het account pagina.
    path('account/', views.account, name='web-account'),

    #Dit is de URL naar de over-ons pagina.
    path('about/', views.about, name='web-about'),
]