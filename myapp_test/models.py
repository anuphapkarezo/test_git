from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class product_masters(models.Model):
    pd_name = models.CharField(max_length=50,unique=True)
    cat_name = models.CharField(max_length=5,default="")
    def __str__(self):
        return self.pd_name + " " + self.cat_name

class Table_members(models.Model):
    member_id = models.CharField(max_length=5,unique=True)
    member_name = models.CharField(max_length=255)
    member_surname = models.CharField(max_length=255)

class Table_login(models.Model):
    user_login = models.CharField(max_length=30)
    pass_login = models.CharField(max_length=30)
    remark_login = models.CharField(max_length=100)