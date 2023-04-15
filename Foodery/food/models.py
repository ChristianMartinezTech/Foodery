"""Food App Model/Database file"""


from django.db import models


class Restaurant(models.Model):
    """A model for Each Restaurant in Foodery"""
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=150) # Colombian, Itallian, French, Japanesse
    image = models.CharField(max_length=500, default="food/static/food/images/restaurant_placeholder.avif")
    #picture = models.ImageField()
    
    # Restaurant String method
    def __str__(self):
        return "%s - %s" % (self.name, self.type)

class Plate(models.Model):
    """A model for plates"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    image = models.CharField(max_length=500, default="food/static/food/images/food_placeholder.png")

    # Plate String method
    def __str__(self):
        return "%s - %s %s: %s %s" % (self.restaurant, self.name, self.description, self.price, self.available)
