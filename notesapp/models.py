
from django.db import models

# Create your models here.


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=255)