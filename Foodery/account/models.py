"""Account App models"""


from django.db import models
from food.models import Plate


# Account Class model
class Account(models.Model):
    """Model for each Account in Foodery"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.email, self.phone)

# Cart Class model
class Cart(models.Model):
    """Model for cart functionality"""
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    order = models.ForeignKey(Plate, on_delete=models.PROTECT)

    def __str__(self):
        return "%s - %s" % (self.account, self.order)
