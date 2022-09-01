from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request): # template의 namespace 여기에 나옴, articles를 앞에 붙여줌
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 여기에 받아온 input 저장하는 로직 들어가야 함
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # return render(request, 'articles/index.html')
    # redner ! = 요청
    # creat하고 index.html을 띄워달란 뜻
    # 근데 index에 context를 넘겨주지 않으니까 index를 요청한 게 아님
    # 그래서 아무것도 안 나옴
    # 원하는 것 : 다시 index 함수를 타서 context 넘겨줬으면 좋겠음
    # 문제 2 : 주소는 여전히 articles/index가 아니라 create 유지 -> 요청한 게 아니라 껍데기만 띄운 거니까
    
    return redirect('articles:detail', article.pk) # 여기로 갈게!

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# 실제로 수정하려면 아래 두 함수가 2개 필요
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk) ## 일단 가져오고 생각
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk) # 수정하고 detail페이지 바로 가게