from django.shortcuts import render, redirect
from .models import Vote
from .forms import VoteForm

from .models import Vote, Comment
from .forms import VoteForm, CommentForm

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes': votes
    }
    return render(request, 'votes/index.html', context)


def create(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    else:
        form = VoteForm()
    context = {
        'form': form,
    }
    return render(request, 'votes/create.html', context)


def detail(request, pk):
    vote = Vote.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = vote.comment_set.all()

    cnt_blue = 0
    cnt_red = 0

    for comment in comments:
        if comment.pick == 'BLUE':
            cnt_blue += 1
        elif comment.pick == 'RED':
            cnt_red += 1

    percent_b = round(cnt_blue / (cnt_blue + cnt_red) * 100, 2)
    percent_r = 100 - percent_b

    context = {
        'vote': vote,
        'comment_form': comment_form,
        'comments': comments,
        'percent_b': percent_b,
        'percent_r': percent_r,
    }
    return render(request, 'votes/detail.html', context)


def comments_create(request, pk):
    vote = Vote.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.vote = vote
        comment.save()

    return redirect('votes:detail', vote.pk)