from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL



class Collections(models.Model):
    name = models.CharField(max_length=50, default='Collection')


class Note(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(Collections, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 40)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length = 170)
    is_important = models.BooleanField(null=True)

    class Meta:
        ordering = ['-date']
