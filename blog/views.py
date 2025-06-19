from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import Post,Aboutus
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
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
            send_mail(subject,message,'noreplay@blog.com',[sendemail])
            return render(request,"contact.html",{"form":form})
        else:
            return render(request,"contact.html",{"form":form,"name":name,"email":email,"message":message})
    return render(request,"contact.html")

