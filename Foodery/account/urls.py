"""Account App urls file"""


from django.urls import path
from . import views


app_name = 'account'

# Defining Food App URLs
urlpatterns = [
    path('', views.index, name="index"),
]