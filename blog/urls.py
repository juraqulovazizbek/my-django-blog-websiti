from django.urls import path

from .views import(
    HomeView,
    BlogView,
    BlogDetailView, 
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blogs/<slug:slug>', BlogDetailView.as_view(), name='home_detail'),
]
