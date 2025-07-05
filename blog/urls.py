from django.urls import path
from . import views

app_name="blog"
urlpatterns=[
    path("",views.index,name="index"),
    path("post/<str:slug>",views.details,name="details"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logout",views.userlogout,name="logout")
]