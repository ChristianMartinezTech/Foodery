# Generated by Django 4.1.7 on 2023-04-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_plate_picture_remove_restaurant_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='image',
            field=models.CharField(default='/home/chrismartinez/Python/django/udemy/Foodery/Foodery/food/static/food/images/food_placeholder.png', max_length=500),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default='/home/chrismartinez/Python/django/udemy/Foodery/Foodery/food/static/food/images/restaurant_placeholder.avif', max_length=500),
        ),
    ]
