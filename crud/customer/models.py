from django.db import models

class Customer(models.Model):
    cid=models.CharField(max_length=20)
    cname=models.CharField(max_length=100)
    cemail=models.EmailField()
    ccontact=models.CharField(max_length=15)

    def __str__(self):
        return "%s" %(self.cname)
    
    class meta:
        db_table="customer"
