from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name='profile') #Imports the overrode User from settings, not directly from other app. This way the Recipes app is standalone.
    avatar = models.ImageField(upload_to='media/avatars/', default='defaults/avatar.jpg')
    bio = models.TextField(null=True, blank=True)
    joined = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            img = img.convert("RGB")
            img.thumbnail((50, 50))
            img.save(self.avatar.path)
            
    def __str__(self): #If portrayed in a string, it returns the users username, followed by: 's profile
        return f"{self.user.username}'s profile"
    
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name='recipe')
    image = models.ImageField(upload_to='media/recipes/')
    title = models.CharField(max_length=255)
    instructions = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self): #If portrayed in a string, it returns the recipe's title
        return self.title
    
    class Meta:
        ordering = ['-date_added'] #Orders the dates backwards, so new recipes with newer dates are added on top