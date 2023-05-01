"""File to have all the food App Views  (functions)"""


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant, Plate
from .forms import PlateForm


# Index View
def index(request):
    # Getting Restaurants and Plates
    restaurant_list = Restaurant.objects.all()
    plates_list = Plate.objects.all()
    
    #template = loader.get_template('food/index.html') Getting HTML template

    # creating context
    context = {
        'restaurant_list': restaurant_list,
        'plates_list': plates_list,
    }
    
    return render(request, 'food/index.html', context) # Remdering request, template, and context


# Greeting View
def hello(request):
    return HttpResponse("Hi there! Thank you for using Foodery. :)") # Way to not use context


# Restaurants View
def restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }

    return render(request, 'food/restaurants.html', context)


# Plates View
def plates(request):
    plates = Plate.objects.all()
    context = {
        'plates': plates,
    }

    return render(request, 'food/plates.html', context)


# Restaurant detail view
def restaurant_detail(request, restaurant_id):

    restaurant_detail = Restaurant.objects.get(pk=restaurant_id)
    plates_list = Plate.objects.filter(restaurant=Restaurant.objects.get(pk=restaurant_id))

    # template = loader.get_template('food/restaurant-detail.html') Getting HTML template
    
    # creating context
    context = {
        'restaurant_detail': restaurant_detail,
        'plates_list': plates_list,
    }
    
    return render(request, 'food/restaurant-detail.html', context)


# Plate detail view
def plate_detail(request, plate_id, restaurant_id):
    
    restaurant_detail = Restaurant.objects.get(pk=restaurant_id)
    plate_detail = Plate.objects.get(id=plate_id)

    context = {
        'restaurant_id': restaurant_detail,
        'plate_detail': plate_detail,
    }

    return render(request, 'food/plate-detail.html', context)


# Cart detail view
def cart(request):
    form = PlateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food/index.html')
    
    context = {
        'form': form,
    }

    return render(request, 'food/cart.html', context)


# Account detail view
def account(request):
    context = {}
    return render(request, 'food/account.html', context)
