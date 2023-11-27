from django.db import models
from django.contrib.auth.models import AbstractUser

class Profil(AbstractUser):
    tel = models.CharField(max_length=15, blank=True)
    davlat = models.CharField(max_length=30, blank=True)
    jins = models.CharField(max_length=10, blank=True)
    shahar = models.CharField(max_length=30, blank=True)
    tasdiqlash_kodi = models.CharField(max_length=30, blank=True)
    tasdiqlangan = models.BooleanField(default=False)

    def __str__(self):
        return self.username
