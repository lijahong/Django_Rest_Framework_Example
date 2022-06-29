from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Review(models.Model):
    score = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    contents = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


