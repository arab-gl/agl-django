from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    faction_choices = (
        ('WH', "White"),
        ('DK', "Dark"),
    )
    faction = models.CharField(max_length=2, choices=faction_choices, default='WH')
