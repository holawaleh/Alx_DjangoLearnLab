# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Step 1: Custom User Manager
# class CustomUserManager(BaseUserManager):
    
# class CustomUser(AbstractUser):
    
# Step 3: Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title