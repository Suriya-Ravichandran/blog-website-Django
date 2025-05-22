from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    products=[
        {"id":1,"productname":"Apple","price":300,"quantity":10},
        {"id":2,"productname":"Banana","price":400,"quantity":10},
        {"id":3,"productname":"Graphs","price":100,"quantity":15},
        {"id":4,"productname":"Orange","price":300,"quantity":9},
        {"id":5,"productname":"Mango","price":500,"quantity":8},
        {"id":6,"productname":"Pine apple","price":500,"quantity":8},
    ]

    return render(request,"index.html",{"products":products})
