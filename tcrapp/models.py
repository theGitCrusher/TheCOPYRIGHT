from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    description = models.TextField()
    category = models.CharField(max_length=20, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_image', default='')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.product_name