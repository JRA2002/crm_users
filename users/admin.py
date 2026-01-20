from django.contrib import admin
from .models import Product, Claim  

# Register your models here.
admin.site.register(Product)
admin.site.register(Claim)