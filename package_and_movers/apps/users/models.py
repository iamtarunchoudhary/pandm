from django.db import models

# Create your models here.

class AppUsers(models.Model):
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12)
    facebook_id = models.CharField(max_length=500)
    google_id = models.CharField(max_length=500)
    status = models.BooleanField(max_length=None) 
    created = models.DateTimeField('date published')
    updated = models.DateTimeField('updated date')

