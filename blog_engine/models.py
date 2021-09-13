from django.db import models
import datetime

class BlogModel(models.Model):
    Heading = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now())
    body = models.TextField(null=True, default="whatever...")

    def __str__(self):
        return self.Heading
