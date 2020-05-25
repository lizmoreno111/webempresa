from django.shortcuts import render
from .models import Post, Category

# Create your views here.

posts = Post.objects.all()
def blog(request):
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, "blog/category.html", {'category':category})