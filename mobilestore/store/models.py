from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=120)
    model=models.CharField(max_length=120)
    image=models.ImageField(upload_to='product_images',null=True,blank=True)
    price=models.IntegerField()
    color=models.CharField(max_length=120)
    description=models.CharField(max_length=300)
