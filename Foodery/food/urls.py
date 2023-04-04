"""food App urls file"""


from django.urls import path
from . import views


# Defining Food App URLs
urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('item/', views.item, name='item'),
]