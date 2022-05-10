from django.urls import path
from .views import blog,home,about

urlpatterns = [
    path('', home, name="home"),
    path('blog', blog, name="blog"),
     path('about', about, name="about"),
]