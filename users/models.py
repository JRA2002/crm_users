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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False, null=True, help_text="Title of your problem")
    motive = models.CharField(max_length=10, choices=CHOICES)
    description = models.TextField(max_length=150, help_text="Describe your problem ...")
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
