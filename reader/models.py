from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Account(AbstractUser):
    u_type = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)
    names_of_books = models.CharField(max_length=200,null=True)
    categories = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=14,null=True)


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    preferred_categories = models.CharField(max_length=100)
    preferred_writers = models.CharField(max_length=100)
    Adress = models.CharField(max_length=100)
    u_id = models.CharField(max_length=500)

class SystemAdmin(models.Model):
    system_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=500)