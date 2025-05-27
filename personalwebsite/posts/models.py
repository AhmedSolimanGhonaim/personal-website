from django.db import models
from django.utils import timezone
from django.urls import reverse
class Posts(models.Model):
    text = models.CharField(max_length=400)
    title = models.CharField(max_length=100, default="Untitled Post")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.pk})
    
    class Meta:
        ordering = ["-created_at"]