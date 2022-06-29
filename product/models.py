from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)