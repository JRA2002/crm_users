from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Claim(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    date_claim = models.DateField()
    date_finish = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
