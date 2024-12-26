from django.db import models

# Create your models here.
class LoginTable(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    PassWord = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

class UserTable(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone =models.IntegerField(null=True, blank=True)

    

class ManufactureTable(models.Model):
    CompanyName = models.CharField(max_length=100, null=True, blank=True)
    CompanyAddress = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    phone =  models.IntegerField(null=True, blank=True)

class ProductTable(models.Model):
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductType = models.CharField(max_length=100, null=True, blank=True)
    Manufacturedate = models.DateField(null=True, blank=True)
    Expirydate = models.CharField(max_length=100, null=True, blank=True)
    Uplaodphoto = models.FileField(max_length=250, null=True, blank=True,upload_to='Media')
    Productprice = models.IntegerField(null=True, blank=True)
     
class FeedBack(models.Model):
    FeedBack = models.CharField(max_length=250, null=True, blank=True)
    Rating = models.FloatField( null=True, blank=True)