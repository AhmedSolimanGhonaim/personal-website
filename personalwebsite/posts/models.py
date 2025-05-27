from turtle import mode
from django.db import models

class Posts (models.Model):
    text = models.CharField(max_length=400)


    
    
    def __str__(self):
        return self.text[:50]

post = Posts.objects.all()