from email import message
from unicodedata import category
from django.http import HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article, Category, Feedback 
# from blog.models import *
from staff.forms import CategoryForm, ReplyFeedbackForm
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def dashboard(request):

    total_categories = Category.objects.count()
    total_articles =Article.objects.count()
    feedback = Feedback.objects.all()

    context = {

        "total_articles": total_articles,
        "total_categories": total_categories,
        "messages": feedback
    }

    return render (request, "dashboard.html", context)

def categories(request):

    categories = Category.objects.all() 

    context = {
        "categories" : categories
    } 

    return render(request, "category.html", context)

def articles(request):

    articles = Article.objects.all()

    context = {
        "articles" : articles
    }  

    return render(request, "articles.html", context)  

## Class based Views
class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles.html" 

class ArticleCreateView(CreateView):
    model= Article
    success_url = "/staff/articles"
    template_name ="article_form.html"
    #fields = '__all__'
    fields = ["picture", "status", "title", "content", "writer", "category"] 

class ArticleUpdateView(UpdateView):
    model= Article
    success_url = "/staff/articles"
    template_name ="article_form.html"
    #fields = '__all__'
    fields = ["picture", "status", "title", "content", "writer", "category"] 
    
def deleteArticle(request, id):

    try:
        article = Article.objects.get(pk=id)  

    except Article.DoesNotExist:

        return JsonResponse({"success": False})

    article.delete()

    data = {
        "success": True
    } 

    return JsonResponse(data)   

def replyFeedback(request, id):

    feedback = Feedback.objects.filter(pk=id).first()

    if request.method == "GET":

        form = ReplyFeedbackForm()
      

        context = {
            "form": form,
            "feedback": feedback
        }  

        return render (request, 'feedback_reply.html', context) 

    else:

        form = ReplyFeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            ## send mail(subject,message, from, [list of recipients])
            send_mail(

                subject,
                message,
                "admin@gmail.com",
                [feedback.email]
            )    

        return HttpResponseRedirect('/staff/feedback')  

def feedback(request):

    messages = Feedback.objects.all()

    return render(request, "feedback.html", {'messages': messages})   

def createCategory(request):

    if request.method == "GET":
        form = CategoryForm()
        action = "Create" 

        context = {

            "action": action,
            "form": form
        }  

        return render(request, "category_form.html", context)    

    else:

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/staff/categories')  

def deleteCategory(request, id):

    category = Category.objects.filter(pk=id).first()
    category.delete()

    data = {
        "success": True
    }

    return JsonResponse(data)      