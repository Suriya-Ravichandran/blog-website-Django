from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("postdetails/<str:post_id>",views.postdetails,name="postdetails"),
]