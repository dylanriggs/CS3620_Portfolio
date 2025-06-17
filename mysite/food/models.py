from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
            return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.Ygxe4M39-El0f3HPLQOmWQHaHa?w=191&h=191&c=7&r=0&o=7&pid=1.7&rm=3")