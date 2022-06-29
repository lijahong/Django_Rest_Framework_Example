from django.db import models

# Create your models here.

class Review(models.Model):
    score = models.IntegerField()
    contents = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)