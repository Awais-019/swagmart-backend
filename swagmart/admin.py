from django.contrib import admin
from .models import Collection, Product, Promotion

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'collection', 'price', 'inventory')
    list_editable = ('price', 'inventory')
    list_per_page = 10
    search_fields = ('name', 'collection__name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Collection)
admin.site.register(Promotion)
