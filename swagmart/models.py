from django.db import models

# Create your models here.

class Collection(models.Model):
    AUDIENCE_CHOICES = [
        ('men', "Men"),
        ('women', "Women")
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    target_audience = models.CharField(max_length=5, choices=AUDIENCE_CHOICES)
    featured_product = models.ForeignKey('Product', on_delete=models.CASCADE, 
                                         null=True, blank=True, related_name='featured_product')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Collections'
        verbose_name = 'Collection'
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='productImages')

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name_plural = 'Product Images'
        verbose_name = 'Product Image'

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    discount = models.FloatField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Promotions'
        verbose_name = 'Promotion'