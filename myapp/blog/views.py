from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello world</h1>")


def postdetails(request,post_id):
    return HttpResponse(f"<h1> Post details page {post_id} </h1>")