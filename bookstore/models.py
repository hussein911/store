from django.db import models
from reader.models import Account,SystemAdmin

# Create your models here.
class BookStore(models.Model):
    bookstore_id=models.AutoField(primary_key=True)
    address=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    bio=models.CharField(max_length=1000)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    system=models.ForeignKey(SystemAdmin,on_delete=models.CASCADE)

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    date=models.DateField()
    photo=models.ImageField()
    description=models.CharField(max_length=1000)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    bstore=models.ForeignKey(BookStore,on_delete=models.CASCADE)
