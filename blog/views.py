from django.shortcuts import render
from django.http import HttpResponse
from .models import Info, Article
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def home(request):

    about = Info.objects.filter(Q(id=1))
    top = Article.objects.all().order_by("-id")[:1]
    blogs = Article.objects.all().order_by("-id")[1:3]
    return render(request, 'Home.html',{'name':about, 'blogs' : blogs, 'top' : top})

def blog(request):

    return render(request, 'blog.html')

def filtered(request):

    top = Article.objects.all().order_by("-id")[:1]
    blogs = Article.objects.all().order_by("-id")[1:]
    return render(request, 'filter.html', {'blogs' : blogs, 'top' : top})

def addpost(request):

    if(request.method == "POST"):
        if request.POST.get('heading') and request.POST.get('date'):
            article = Article()
            article.Heading=request.POST.get("heading")
            article.Date=request.POST.get("date")
            article.Brief=request.POST.get("brief")
            article.Desc=request.POST.get("desc")
            article.save()
            messages.info(request, 'Post added successfully')
            print(messages)
        return render(request, 'addpost.html', {'message' : messages})
    return render(request, 'addpost.html')