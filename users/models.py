from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=1000, unique=True, verbose_name="Foydalanuvchi nomi")
    first_name = models.CharField(max_length=1000, verbose_name="Ismi")
    last_name = models.CharField(max_length=1000, verbose_name="Familiyasi")
    middle_name = models.CharField(max_length=1000, verbose_name="Otasining ismi")
    city = models.CharField(max_length=1000, verbose_name="Shahar")
    town = models.CharField(max_length=1000, verbose_name="Tuman")
    rural = models.CharField(max_length=1000, verbose_name="Qishloq")
    school = models.CharField(max_length=1000, verbose_name="Maktab nomi")
    image = models.ImageField(upload_to="images/users", null=True, blank=True, verbose_name="Rasm")
    point = models.IntegerField(default=0, verbose_name="Ball")

    is_student = models.BooleanField(default=False, verbose_name="O'quvchi")
    is_active = models.BooleanField(default=False, verbose_name="Faol")

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username    
