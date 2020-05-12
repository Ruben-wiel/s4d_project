from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-overons'),
    path('posts/', views.posts, name='web-posts'),
    path('account/', views.account, name='web-account'),
]