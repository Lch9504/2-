from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=55)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
