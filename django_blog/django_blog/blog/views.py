from django.shortcuts import render

def home(request):
    return render(request, "blog/base.html")

def posts(request):
    return render(request, "blog/posts.html")  # create this template later
