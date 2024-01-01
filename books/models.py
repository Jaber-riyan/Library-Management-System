from django.db import models
from django.contrib.auth.models import User
from categories.models import CategoryModel

# Create your models here.

class BookModel(models.Model):
    book_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()
    book_price = models.IntegerField(default=0)
    book_image = models.ImageField(upload_to='books/media/uploads/', blank=True , null=True)
    category = models.ManyToManyField(CategoryModel)
    queantity = models.IntegerField(default=20, null=True, blank=True)
    
    def __str__(self):
        return self.book_name
    
    
class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name='user')
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    
    
    def __str__(self):
        return self.user.username
    


    
    
class BorrowHistoryModel(models.Model):
    book_name = models.CharField(max_length=55)
    price = models.CharField(max_length=55)
    category = models.CharField(max_length=155)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    after_decreament = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.book_name
