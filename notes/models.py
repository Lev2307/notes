from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL



class Collection(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, default='Collection')

    def __str__(self):
        return self.name
        

class Note(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
<<<<<<< HEAD
    collection = models.ForeignKey(Collection, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 30)
    date = models.DateField(auto_now=True)
    text = models.CharField(max_length = 150)
    is_important = models.BooleanField(null=True, default=False)
=======
    collection = models.ForeignKey(Collections, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length = 40)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length = 170)
    is_important = models.BooleanField(null=True)
>>>>>>> e3100fe602e09f1c09d67c326c8f436966f2f403

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.header
