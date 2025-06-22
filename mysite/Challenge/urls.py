from . import views
from django.urls import path

app_name = 'challenge'
urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/<int:item_id>', views.p_detail, name="p_detail"),
    path('hobbies/<int:item_id>', views.h_detail, name="h_detail"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('contact', views.contact, name="contact"),
    path('update/<int:id>', views.update_portfolio, name="update_portfolio"),
    path('add', views.create_portfolio, name="create_portfolio"),
    path('delete/<int:id>', views.delete_portfolio, name="delete_portfolio"),
]