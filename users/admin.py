from django.contrib import admin
from .models import Client, Product, Claim

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Claim)