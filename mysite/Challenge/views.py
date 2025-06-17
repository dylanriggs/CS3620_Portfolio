from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies

def home(request):
    return render(request, 'challenge/index.html')

def portfolio(request):
    project_list = Portfolio.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'challenge/portfolio.html', context)

def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'challenge/hobby.html', context)

def contact(request):
    return render(request, 'challenge/contact.html')

def p_detail(request, item_id):
    project = Portfolio.objects.get(pk=item_id)
    context = {
        'project' : project
    }
    return render(request, 'challenge/p_detail.html', context)

def h_detail(request, item_id):
    hobby = Hobbies.objects.get(pk=item_id)
    context = {
        'hobby' : hobby
    }
    return render(request, 'challenge/h_detail.html', context)
