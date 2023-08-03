from django.db import models

# Create your models here.

"""seleccionas todo lo que se quiere comentar ctrl+}"""
# class Tasks(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60)
#     desc = models.CharField(max_length=255)



class Regist(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    
    class Meta:
        db_table : 'Regist'
   