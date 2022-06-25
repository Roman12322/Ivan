from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)

class Calc(models.Model):
    user_id = models.CharField(max_length=1000, null=True)
    First_Up = models.CharField(max_length=1000, null=True)
    First_Dwn = models.CharField(max_length=1000, null=True)
    Second_Up = models.CharField(max_length=1000, null=True)
    Second_Dwn = models.CharField(max_length=1000, null=True)
    Answer_Up = models.CharField(max_length=1000, null=True)
    Answer_Dwn = models.CharField(max_length=1000, null=True)
