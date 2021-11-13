from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, default='dpt')
    image = models.CharField(max_length=100, default='dpt.jpg')

    def __str__(self):
        return self.name

