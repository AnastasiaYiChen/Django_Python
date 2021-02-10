from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Eventsview(models.Model):
    conference = models.ForeignKey(Post, on_delete=models.CASCADE)
    events_name = models.CharField(max_length=100)
    events_description = models.CharField(max_length=100)
    events_location = models.CharField(max_length=1000)
    up_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.events_name

class Selection(models.Model):
    tag = models.CharField(max_length=100)
    conference_preference = models.TextField()

