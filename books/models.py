from django.db import models

# Create your models here.
from reader.models import Account
from bookstore.models import BookStore

class Books(models.Model):
    Book_id = models.AutoField(primary_key=True)
    Price = models.FloatField()
    Year = models.DateField()
    edition = models.IntegerField()
    Photo = models.ImageField()
    Writer_name = models.CharField(max_length=50)
    Book_name = models.CharField(max_length=50)
    Book_type = models.IntegerField()
    Book_category = models.CharField(max_length=150)

class secondhand_books(models.Model):
    ID = models.ForeignKey(Books, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=14)

class Bookstore_books(models.Model):
    BookStore_name = models.CharField(max_length=50)
    out_of_stock = models.BooleanField()
    Book_id=models.ForeignKey(Books,on_delete=models.CASCADE )
    store_id=models.ForeignKey(BookStore,on_delete=models.CASCADE)

#secondbooks that are sold or bought by user
class Books_of_user(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    secondbook=models.ForeignKey(secondhand_books,on_delete=models.CASCADE)

#newbooks that users are bought
class StoreBooks_of_user(models.Model):
    newuser=models.ForeignKey(Account,on_delete=models.CASCADE)
    newbook=models.ForeignKey(Bookstore_books,on_delete=models.CASCADE)