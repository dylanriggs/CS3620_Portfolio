# Generated by Django 5.2.2 on 2025-06-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_name', models.CharField(max_length=200)),
                ('portfolio_desc', models.CharField(max_length=200)),
            ],
        ),
    ]
