from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


##### Demo codes here #####

# def index(request):
#     return HttpResponse("Hello world")


#### Main code here ####

def index(request):
    return render(request,"index.html")

def python(request):

    posts=[
        {"id":1,"title":"Python introduction","Content":"Demo content 1"},
        {"id":2,"title":"Python Variables","Content":"Demo content 2"},
        {"id":3,"title":"Python Operators","Content":"Demo content 3"},
    ]


    return render(request,"posts.html",{"posts": posts})