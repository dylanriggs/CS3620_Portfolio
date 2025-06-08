from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('contact', views.contact, name="contact"),
]