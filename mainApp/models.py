from django.db import models
from django.contrib.auth.models import User

de ="Lorem ipsum dolor sit amet, nunc eleifend diam porta, amet elit, nullam et, praesent luctus lacus egestas, vehicula sit. Urna sed porttitor malesuada sit quis venenatis, est morbi est fusce, lorem aliquet pede, sodales justo vel diam sit, nunc ultrices maecenas urna. Phasellus volutpat a orci, wisi consectetuer. Turpis et vitae. Maecenas a. Amet ridiculus suspendisse sociis nunc tortor, wisi a justo nullam, mauris lorem turpis et. Ut pede quisque vestibulum, fusce wisi ac tellus, ut adipiscing integer eget purus lobortis. Lobortis eu, nec consequat quis sed vestibulum eleifend elementum, aptent eu rutrum non vel, dui fusce vehicula senectus magna tempor, lectus nulla."

productType = (
    ("Electronics","Electronics"),
    ("Sport","Sport"),
    ("Book","Book"),
    ("Clothing","Clothing"),

)

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

