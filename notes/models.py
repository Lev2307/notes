from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Note(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 30)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length = 150)
    is_important = models.BooleanField(null=True)


class Collections(models.Model):
    
    notes = models.ManyToManyField(Note)
