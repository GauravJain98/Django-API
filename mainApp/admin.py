from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =('id','name','typeOf','price','quantity')

admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display =('amount',)

admin.site.register(Cart,CartAdmin)

admin.site.register(InCart)
