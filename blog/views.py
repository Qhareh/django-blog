
from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    ## This returns a queryset containing all articles in the database
    articles=Article.objects.filter(status = Article.LIVE).filter(created_at__year = 2022)

    context = {
        "articles": articles
     }

    return render(request, "index.html", context)
    
def blog(request):
    articles=Article.objects.filter(status = Article.LIVE)
    context = {
      
        "articles": articles
    }

    return render(request, "blog.html", context)

def about(request):
    context = {
      
        
    }

    return render(request, "about.html", context)

def contact(request):
    context = {
      
        
    }

    return render(request, "contact.html", context)

def submitContactForm(request):

    if request.method == "POST":
    ## handle form data
      form_data =request.POST
      email = form_data["email"]
      name = form_data["name"]
      number = form_data["number"]
      message = form_data["message"]

 
      return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")
     
def successRedirect(request):
    context = {
     
    }

    return render(request, "success.html", context)

def ajaxContactSubmission(request):
   

    email = request.POST["email"]
    name = request.POST["name"]
    number = request.POST["Phone"]
    message = request.POST["message"]

    feedback= Feedback.objects.create(
        name= name,
        message = message,
        email = email
    )
  
    send_mail(
        "New message",
        "Hi Admin, you have a new message",
        "admin@gmail.com",
        ['admin@gmail.com'],
        fail_silently=False
    )

    context = {
        "success": True,
        "message": "Thank you "  +name+ " for your message"
    }

    return JsonResponse(context)

def getArticleDetails(request, id):

    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:

        messages.info("Sorry, that article does not exist")
        return HttpResponseRedirect("/")

    categories =Category.objects.all()
    all_articles = Article.objects.exclude(pk=id)

    context = {
        "article":article,
        "categories": categories,
        "more_articles": all_articles
    }

    return render(request, "article-details.html", context)    

def searchArticles(request):

    query = request.POST["query"]

    articles = Article.objects.filter(
        status = Article.LIVE).filter(title__contains=query).filter(
            content__contains = query
        )  
        

    context = {
        "articles": articles
    } 

    return render(request, "blog.html", context)   

def redirectAfterLogin(request):

    if request.user.is_superuser:
        ##Redirect to dashboard

        return HttpResponseRedirect("/staff/dashboard")

    else:
        ## Redirect to blogs/posts    

        return HttpResponseRedirect("/blog")      