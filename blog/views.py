from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . models import Post,Aboutus,User
from django.core.paginator import Paginator
from .forms import ContactForm,SignupForm,SigninForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    blog_title="Latest Post"
    allpost=Post.objects.all()
    pagenator=Paginator(allpost,6)
    page_number=request.GET.get("page")
    page_object=pagenator.get_page(page_number)
    return render(request,"index.html",{'blog_title':blog_title,"page_obj":page_object})


def details(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        relatedpost=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exits")
    return render(request,"details.html",{"post":post,"relatedpost":relatedpost})

def about(request):
    aboutcontent=Aboutus.objects.first()
    if aboutcontent is None or not aboutcontent.content:
        aboutcontent="Default content here"
    else:
        aboutcontent=aboutcontent.content
    return render(request,"about.html",{"aboutcontent":aboutcontent})


def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message_form=request.POST.get('message')

        if form.is_valid():
            sendemail="rsuriya119@gmail.com"
            subject="You Got a Enquiry in Blog"
            message=render_to_string("contactemail.html",{
                "name":name,
                "email":email,
                "message":message_form

            })
            messages.success(request,"Form submit successfully")
            send_mail(subject,message,'noreplay@gmail.com',[sendemail])
            return render(request,"contact.html",{"form":form})
        else:
            return render(request,"contact.html",{"form":form,"name":name,"email":email,"message":message_form})
    return render(request,"contact.html")

def signup(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Signup Successfull You can Login")
            return redirect("blog:dashboard")
    return render(request,"signup.html",{"form":form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('blog:dashboard')
    else:
        form = SigninForm()
    
    return render(request, 'signin.html', {'form': form})

def dashboard(request):
    return render(request,"dashboard.html")
