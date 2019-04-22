from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # for 1 to many relationship
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Foe date_posted
    #auto_now=True  => set time when the post was actually created
    #auto_now_add  => set the time to only when this object is created, but can't update its value
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete-> when a user is deleted delete their post also

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
