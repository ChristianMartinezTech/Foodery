# Generated by Django 4.1.7 on 2023-05-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
