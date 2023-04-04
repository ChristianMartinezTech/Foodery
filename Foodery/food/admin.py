"""File to add models to have access to from the Admin console"""


from django.contrib import admin
from .models import Restaurant, Plate


#Models
admin.site.register(Restaurant)
admin.site.register(Plate)
