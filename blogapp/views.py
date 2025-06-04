from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Catagory
# Create your views here.


##### Demo codes here #####

# def index(request):
#     return HttpResponse("Hello world")


#### Main code here ####

def index(request):
    return render(request,"index.html")

def python(request):
    posts=Post.objects.all()
    return render(request,"posts.html",{"posts": posts})

def postdetails(request,id):
   posts=Post.objects.get(pk=id)
   category= posts.category
   return render(request,"postdetails.html",{"posts": posts,"category":category})