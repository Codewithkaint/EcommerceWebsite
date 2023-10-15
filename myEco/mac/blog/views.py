from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Blog
# import json


def index(request):
    blog=Blog.objects.all()
    allBlog=[]
    titId=Blog.objects.values('category','postId')
    blogPost={item["category"] for item in titId}
    for cat in blogPost:
        newPost=Blog.objects.filter(category=cat)
        n=len(newPost)
        x=n%2
        newLine=0
        if(x!=0):
            newLine=1
        newLine+=n//2
        totalBlogs=len(blog)
        allBlog.append([newPost,range(1,newLine),totalBlogs])
    params={'totBlog':allBlog}
    print(params)



    return render (request,'blog/index.html',params)


def post(request,myid):



    post=Blog.objects.filter(postId=myid)
    
    return render(request,'blog/post.html',{'post':post[0]})