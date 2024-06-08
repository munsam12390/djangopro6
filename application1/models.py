from django.db import models
class product_management(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    account=models.IntegerField()
    adress=models.CharField(max_length=30)
    product=models.CharField(max_length=28)

# Create your models here.
