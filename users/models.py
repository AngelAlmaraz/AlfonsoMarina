from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from PIL import Image
import math

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = Department

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            width = math.floor(img.width*300/img.height)
            height = math.floor(img.height * 300 / img.width)
            if img.height > img.width:
                output_size = (300 , width )
            else:
                output_size = (height , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)