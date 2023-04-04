"""File to have all the food App Views  (functions)"""


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant, Plate

# food index view
def index(request):
    # Getting Restaurants and Plates
    restaurant_list = Restaurant.objects.all()
    plates_list = Plate.objects.all()
    
    template = loader.get_template('food/index.html') # Getting HTML template

    # creating fake contest
    context = {
        'restaurant_list': restaurant_list,
        'plates_list': plates_list,
    }
    
    return HttpResponse(template.render(context, request)) # Sending template, context, and request

# Greeting View
def hello(request):
    return HttpResponse("Hi there! Thank you for using Foodery. :)")

# Item view
def item(request):
    return HttpResponse("<h1>this is an item view</h1>")


