from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe


# Create your views here.
@require_safe
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('posts:index')
    return redirect('accounts:login')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update.html', context)