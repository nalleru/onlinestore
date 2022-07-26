from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    product_description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name