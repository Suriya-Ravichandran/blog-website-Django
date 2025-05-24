from django.urls import path
from . import views

app_name= 'myapps'
urlpatterns = [
   path("",views.index,name="index"),
   path("old_url",views.old_url,name="old_url"),
   path("new_url",views.new_url,name="new_url"),
   path("productdetail/<str:product_id>",views.productdetails,name="productdetail")
]