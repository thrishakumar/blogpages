from django.db import models
import datetime


# Create your models here.
class Post(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=40)

    def __str__(self) -> object:
        return self.title
