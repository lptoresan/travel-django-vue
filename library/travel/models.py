from django.db import models
from uuid import uuid4

class Travel(models.Model):
    id_travel = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    price_confort = models.FloatField()
    price_econ = models.FloatField()
    city = models.CharField(max_length=40)
    duration = models.FloatField()
    seat = models.CharField(max_length=3)
    bed = models.CharField(max_length=3)        

class Users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)