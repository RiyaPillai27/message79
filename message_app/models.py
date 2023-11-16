from django.db import models

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.CharField(max_length=50)
    msg=models.CharField(max_length=200)
