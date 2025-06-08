from django.db import models

# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
            return self.hobby_name
    
    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=200)

class Portfolio(models.Model):

    def __str__(self):
            return self.portfolio_name
    
    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=200)