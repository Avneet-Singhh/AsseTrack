from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=150, null= True)
    phone = models.CharField(max_length=20, null=False)
    image = models.ImageField(default='profile.jpg', upload_to='profile')

    def __str__(self) -> str:
        return f'{self.staff.username}-Profile'