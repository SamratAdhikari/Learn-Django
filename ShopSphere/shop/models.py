from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    product_pub_date = models.DateTimeField()

