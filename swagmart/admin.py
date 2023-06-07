from django.contrib import admin
from django.utils.html import format_html
from .models import Collection, Product, Promotion, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" width="100px" height="100px" />')
        return ''

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'collection', 'price', 'inventory')
    list_editable = ('price', 'inventory')
    list_per_page = 10
    search_fields = ('name', 'collection__name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

admin.site.register(Collection)
admin.site.register(Promotion)
