from rest_framework import serializers
from .models import Collection, Product, Promotion, ProductImage

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'target_audience', 'image']

    image = serializers.SerializerMethodField(method_name='get_image_url')

    def get_image_url(self, collection):
        featured_product = collection.featured_product
        if featured_product:
            featured_image = featured_product.images.first()
            if featured_image:
                return  'http://127.0.0.1:8000' + featured_image.image.url
        return None
    
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'inventory', 'images']

    images = serializers.SerializerMethodField(method_name='get_images')

    def get_images(self, product):
        images = product.images.all()
        return ProductImageSerializer(images, many=True).data
        
class CollectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'target_audience', 'products']

    products = serializers.SerializerMethodField(method_name='get_products')

    def get_products(self, collection):
        products = collection.products.all()
        return ProductSerializer(products, many=True).data

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount', 'products']

    products = serializers.SerializerMethodField(method_name='get_products')

    def get_products(self, promotion):
        products = promotion.products.all()
        return ProductSerializer(products, many=True).data