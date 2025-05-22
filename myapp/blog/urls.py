from django.urls import path
from . import views

app_name= 'blog'
urlpatterns=[
    path("",views.index,name="index"),
    path("postdetails/<str:post_id>",views.postdetails,name="postdetails"),
    path("old_url",views.old_url_redirect,name="old_url"),
    path("new_url",views.new_url_redirect,name="new_url"),
]