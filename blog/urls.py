from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('blog', blog, name="blog"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('contact/form/submit', submitContactForm, name="contact.form"),
    path('form/success', successRedirect, name="success.redirect"),
    path("ajax/contact/submission", ajaxContactSubmission, name="contact.ajax.submission"),

    path("article/<id>details", getArticleDetails, name="article.details"),
    path("serach/articles", searchArticles, name="search"),
    path(" login/redirect", redirectAfterLogin, name="login.redirect")
]