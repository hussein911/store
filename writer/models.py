from django.db import models
from reader.models import Account

# Create your models here.
class Writer1(models.Model):
    w_id=models.AutoField(primary_key=True)
    bio=models.TextField(max_length=1000)
    Writer=models.ForeignKey(Account,on_delete=models.CASCADE)

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    Writer_id=models.ForeignKey(Writer1,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)