from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    status = models.IntegerField(choices=(
        (1, "o'quvchi"),
        (2, "o'qtuvchi"),
        (3, "direktor"),
    ))


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'







