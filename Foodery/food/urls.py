"""food App urls file"""


from django.urls import path
from . import views


app_name = 'food'

# Defining Food App URLs
urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('plates/', views.plates, name='plates'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/plate/<int:plate_id>/', views.plate_detail, name='plate_detail'),
    path('cart', views.cart, name="cart"),
    path('account', views.account, name="account"),
]