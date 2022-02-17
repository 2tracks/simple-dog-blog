from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render (request,"blog/templates/index.html", context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post=post
            obj.save()

            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()


    context = {
        'post': post,
        'form': form
    }
    return render (request,"blog/templates/detail.html", context)


def category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'category': category
    }
    return render(request, "blog/templates/category.html", context)
