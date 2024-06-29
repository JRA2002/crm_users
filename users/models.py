from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES = [
    ("Internet", "Internet"),
    ("Mobile", "Mobile"),
    ("TV", "TV"),
    ("Other", "Other"),
]

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class Claim(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    date_claim = models.DateField()
    date_finish = models.DateField()
    status = models.BooleanField()
    
    def __str__(self):
        return self.product
    
