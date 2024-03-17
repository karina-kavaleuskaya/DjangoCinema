from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=False, null=True)
    name = models.CharField(max_length=255, blank=False, null=False)



