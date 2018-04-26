from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        null = False,
        blank = False,
    )
    amount = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.amount)


class InCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete = models.CASCADE,
        null = False,
        blank = False,
    )
    price = models.IntegerField(default=  0)
    def __str__(self):
        return str(self.id)

