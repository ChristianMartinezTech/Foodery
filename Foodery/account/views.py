"""File to have all the Account App views"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Account, Cart
from django.contrib.auth.forms import UserCreationForm

# Account Views
def index(request):
    context = {}
    return render(request, 'account/index.html', context)
