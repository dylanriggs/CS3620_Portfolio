# Generated by Django 5.2.2 on 2025-06-17 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.Ygxe4M39-El0f3HPLQOmWQHaHa?w=191&h=191&c=7&r=0&o=7&pid=1.7&rm=3', max_length=500),
        ),
    ]
