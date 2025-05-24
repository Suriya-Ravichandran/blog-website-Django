from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

products=[
    {"id":1,"productname":"Apple","price":300,"quantity":10},
    {"id":2,"productname":"Banana","price":400,"quantity":10},
    {"id":3,"productname":"Graphs","price":100,"quantity":15},
    {"id":4,"productname":"Orange","price":300,"quantity":9},
    {"id":5,"productname":"Mango","price":500,"quantity":8},
    {"id":6,"productname":"Pine apple","price":500,"quantity":8},
]


def index(request):
    return render(request,"index.html",{"products":products})


def old_url(request):
    return redirect(reverse('myapps:new_url'))
def new_url(request):
    return HttpResponse("This new page")


def productdetails(request,product_id):
    product=next((item for item in products if item["id"] == int(product_id)),None)
    return render(request,"detail.html",{"products":product})