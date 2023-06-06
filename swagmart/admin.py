from django.contrib import admin
from .models import Category, Collection, Product, Promotion

# Register your models here.

admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Promotion)
