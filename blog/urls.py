from django.urls import path

from .views import(
    HomeView,
    BlogView,
    BlogDetailView,
    BlogCreateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blogs/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
]
