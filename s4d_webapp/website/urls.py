from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    # Onderstaande URL-Links zijn in de menubar verwerkt
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-about'),
    path('posts/', PostListView.as_view(), name='web-posts'),
    path('howto/', views.howto, name='web-howto'),

    # Dit is de URL naar het overzicht van de posts.
    path('posts/post/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/post/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),
    path('posts/post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),
    path('posts/user/<str:username>',
         UserPostListView.as_view(), name='user-posts'),
    path('posts/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

# browser zoekt als volgt de url:
# <app>/<model>_<viewtype>.html
