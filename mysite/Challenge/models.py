from django.db import models

# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
            return self.hobby_name
    
    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.kcnWCTmXz1gblj3emSQBDAHaHK?rs=1&pid=ImgDetMain")

class Portfolio(models.Model):

    def __str__(self):
            return self.portfolio_name
    
    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)
    portfolio_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.0peFLquqi8FFO0e9R3aVyQHaFj?rs=1&pid=ImgDetMain")

class Contact(models.Model):

    def __str__(self):
            return self.contact_name
    
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=500)