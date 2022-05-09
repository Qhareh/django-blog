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
    