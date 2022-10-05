from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseForbidden

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:    # 요청 사람이 쓴 사람이면
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


# # 지금은 두 개의 if에서 튕겼을 때 다 redirect 여기로 오지만, 상태코드에 따라 맞춰 보내주는 것이 필요!
# # @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:   # 1. 인증 되지 않았음을 상태코드로 알려주기
#         if request.user == article.user:    # 2. 인증은 되었으나 이걸 지울 권한이 없음을 알려주기
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()  # 2
#     return HttpResponse(status=401) # 1


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:    # 동일인물인지 확인
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:   # 남의 글을 수정하려고 하면, 메인 페이지로
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


## comment_pk와 article_pk를 따로 가져오지 않고, comment_pk만 인자로 받는 경우
# def comments_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)