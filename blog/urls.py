from django.urls import path
from .views import blog,home

urlpatterns = [
    path('', home, name="home"),
    path('blog', blog, name="blog"),
]