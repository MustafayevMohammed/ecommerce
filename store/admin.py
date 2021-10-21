from django.contrib import admin
from django.db.models.deletion import CASCADE
from .models import *
# Register your models here.

admin.site.register(Product)

admin.site.register(OrderItem)

admin.site.register(Cart)

admin.site.register(Category)
