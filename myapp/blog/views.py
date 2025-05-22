from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'index.html')


def postdetails(request,post_id):
    return HttpResponse(f"<h1> Post details page {post_id} </h1>")

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))
def new_url_redirect(request):
    return HttpResponse("This is new url page")