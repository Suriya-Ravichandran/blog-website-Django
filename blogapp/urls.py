from django.urls import path
from . import views
app_name='blogapp'

urlpatterns = [
    path("",views.index,name="index"),
    path("python",views.python,name="python"),
    path("postdetials/<str:id>",views.postdetails,name="postdetails")
]
