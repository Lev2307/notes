from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Note(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 30)
    date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length = 200)
    is_important = models.BooleanField(null=True)

