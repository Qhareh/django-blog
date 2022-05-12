from django.http import HttpResponseRedirect
from django.shortcuts import render
 
from .models import Writer

# Create your views here.
def home(request):

    user = Writer("John", "Macharia")

    context = {
        "first_name": 'cynthia',
        "last_name": 'khareh',
        "writer": user,
        
    }

    return render(request, "index.html", context)
    
def blog(request):
    context = {
      
        
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