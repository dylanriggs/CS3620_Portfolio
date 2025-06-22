from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
from django.template import loader
from .forms import PortfolioForm, ContactForm

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('challenge:portfolio') 
    else:
        form = ContactForm()

    return render(request, 'challenge/contact.html', {'form': form})

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

def update_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=portfolio)

    if form.is_valid():
        form.save()
        return redirect('challenge:portfolio')
    
    return render(request, 'challenge/portfolio-form.html', {'form': form, 'portfolio':portfolio})

def create_portfolio(request):
    form = PortfolioForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('challenge:portfolio')
    
    return render(request, 'challenge/portfolio-form.html', {'form':form})

def delete_portfolio(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('challenge:portfolio')
    
    return render(request, 'challenge/portfolio-delete.html', {'item':item})