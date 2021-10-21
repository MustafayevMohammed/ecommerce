from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40,verbose_name="Adi:")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=75,verbose_name="Mehsulun adi:")
    description = models.TextField(verbose_name="Aciqlama")
    price = models.FloatField(verbose_name="Qiymet:")
    category = models.ForeignKey(Category,on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name="Orders",verbose_name="Malin sahibi:",on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False,verbose_name="Sifaris bitib?:")
    products = models.ManyToManyField(OrderItem)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Sebetin yaranma tarixi:")

