from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): #to override and extend user
    #Here we add stuff to the user model
    email = models.EmailField(unique=True)
