from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import Post
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    blog_title="Latest Post"
    allpost=Post.objects.all()

    pagenator=Paginator(allpost,2)
    page_number=request.GET.get("page")
    page_object=pagenator.get_page(page_number)


    return render(request,"index.html",{'blog_title':blog_title,'allpost':allpost,"page_obj":page_object})


def details(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        relatedpost=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exits")
    return render(request,"details.html",{"post":post,"relatedpost":relatedpost})

