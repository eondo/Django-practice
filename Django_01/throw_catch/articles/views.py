import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    today = datetime.datetime(2022, 8, 8, 10, 2)
    context = {
        'name': 'Bob', 
        'foods': ['salmon', 'chicken', 'tuna'],
        'today': today
    }

    return render(request, 'greeting.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '김도언':
            message = '교육생이시군요!'
        else:
            message = '교수님이시군요!'
    else:
        message = '다른 반이시군요!'
    
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)


def show(request, name):
    context = {
        'name': name
    }
    return render(request, 'show.html', context)