from django.db import models

# Create your models here.
class Category(models.Model):
    AUDIENCE_CHOICES = [
    ('men', 'Men'),
    ('women', 'Women')
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    target_audience = models.CharField(max_length=255, choices=AUDIENCE_CHOICES)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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
    
class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    discount = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Promotions'
        verbose_name = 'Promotion'