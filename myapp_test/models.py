from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class product_masters(models.Model):
    pd_name = models.CharField(max_length=50,unique=True)
    cat_name = models.CharField(max_length=5,default="")
    def __str__(self):
        return self.pd_name + " " + self.cat_name
