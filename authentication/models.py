from django.db import models

# Create your models here.


# ab hmne ye do cheeje add delete update read iski permission de di hai
class Blog(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)