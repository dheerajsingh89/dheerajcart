from django.db import models
from unicodedata import category
from unittest.util import _MAX_LENGTH
from email.policy import default
from email.mime import image
class Product(models.Model):
    id=models.AutoField
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    product_name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    date=models.DateField()
    image=models.ImageField(upload_to="media/shop/imgs",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name
# Create your models here.
