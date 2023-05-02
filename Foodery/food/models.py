"""Food App models"""


from django.db import models


class Restaurant(models.Model):
    """Model for Each Restaurant in Foodery"""
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=150) # Colombian, Itallian, French, Japanesse
    image = models.CharField(max_length=500, default="https://cdn0.iconfinder.com/data/icons/map-and-location-16/512/restaurant-cup-food-location-lunch-map-restaurant-512.png")
    #picture = models.ImageField()
    
    # Restaurant String method
    def __str__(self):
        return "%s - %s" % (self.name, self.type)

class Plate(models.Model):
    """Model for plates"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=500, default="https://goodviewvictoria.com/img/placeholders/comfort_food_placeholder.png")

    # Plate String method
    def __str__(self):
        return "%s - %s %s: %s %s" % (self.restaurant, self.name, self.description, self.price, self.available)
