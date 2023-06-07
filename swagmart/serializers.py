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

        