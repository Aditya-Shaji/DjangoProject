from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=50)
class Category(models.Model):
    category=models.CharField(max_length=50)
class Register(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)

class Place(models.Model):
    name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
class Subcategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
class Brand(models.Model):
    name=models.CharField(max_length=50)
    

    #on_delete=models.CASCADE place and district data deleted
    #on_delete=models.SET_NULL,null=True place data not deleted just null