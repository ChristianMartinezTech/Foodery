"""File to have all the food App Views  (functions)"""


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('food/index.html') # Getting HTML template
    context = {} # creating fake contest
    return HttpResponse(template.render(context, request)) # Sending template, context, and request

# Greeting View
def hello(request):
    return HttpResponse("Hi there! Thank you for using Foodery. :)")

# Item view
def item(request):
    return HttpResponse("<h1>this is an item view</h1>")


