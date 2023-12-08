from django.db import models
from Admin.models import*
# Create your models here.
class UserRegistration(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField(null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    dob=models.DateField(null=True)
    file=models.FileField(upload_to='userdocs/',null=True)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE,null=True)
