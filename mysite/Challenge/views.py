from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies

def home(request):
    return HttpResponse("""
        <h1>Welcome! - Dylan Riggs</h1>
        <p>I'm a management trainee leading the Shipping & Receiving team at a 3PL cold storage warehouse. I transitioned from food service into logistics, where I developed a passion for process improvement, data-driven decision-making, and empowering people to grow.</p>
        <p>I'm currently pursuing a Bachelor's in Computer Science, with plans to continue into an MBA. I enjoy applying tech to solve real-world problems—whether that's building Power BI dashboards, automating workflows, or experimenting with Django.</p>
        <p>Outside of work, I'm a husband and proud father. Being a dad has shaped how I lead—with patience, perspective, and purpose.</p>
    """)

def portfolio(request):
    projects = Portfolio.objects.all()
    
    html = "<h1>Dylan Riggs – Project Portfolio</h1><ul>"
    for project in projects:
        html += f"<li><strong>{project.portfolio_name}</strong><br>{project.portfolio_desc}</li>"
    html += "</ul>"

    return HttpResponse(html)

def hobbies(request):
    hobbies = Hobbies.objects.all()
    
    html = "<h1>Dylan Riggs – Hobbies</h1><ul>"
    for hobbies in hobbies:
        html += f"<li><strong>{hobbies.hobby_name}</strong><br>{hobbies.hobby_desc}</li>"
    html += "</ul>"

    return HttpResponse(html)

def contact(request):
    return HttpResponse("dylanriggs@mail.weber.edu")

