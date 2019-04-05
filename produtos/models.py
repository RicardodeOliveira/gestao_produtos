from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=30)
    product_amount = models.IntegerField()
    product_value = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.product_name