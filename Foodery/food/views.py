"""File to have all the food App Views  (functions)"""


from django.shortcuts import render
from django.http import HttpResponse


# Greeting View
def hello(request):
    return HttpResponse("Hi there! Thank you for using Foodery. :)")

# Item view
def item(request):
    return HttpResponse("<h1>this is an item view</h1>")


