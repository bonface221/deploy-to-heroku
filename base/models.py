from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='images')
    image = CloudinaryField('deploy-images',folder='new-heroku')
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username