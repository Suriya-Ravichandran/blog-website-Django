from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.
def index(request):
    blog_title="Latest Post"
    allpost=Post.objects.all()
    return render(request,"index.html",{'blog_title':blog_title,'allpost':allpost})

def details(request,slug):
    return render(request,"details.html")

