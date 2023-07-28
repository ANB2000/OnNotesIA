
from uuid import uuid4
from django.db import models

# Create your models here.

"""seleccionas todo lo que se quiere comentar ctrl+}"""
class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=255)

# class Tarea(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     gustos = models.CharField(max_length=150)
#     seleccion = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=90)

#     class Meta: 
#         verbose_name = 'tarea'
#         verbose_name_plural = 'tarea'
#         db_table = 'Tarea'
