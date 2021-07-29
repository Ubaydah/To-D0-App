from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):

    name = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))


    def __str__(self):
        return self.name