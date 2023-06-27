from django.http import HttpResponse
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Collection, Product, Promotion
from .serializers import CollectionSerializer, CollectionDetailSerializer, ProductSerializer, \
    PromotionSerializer

# Create your views here.
def index(request):
    return HttpResponse("Server is up and running!")


class CollectionViewSet(ListModelMixin, GenericViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
class CollectionDetailViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionDetailSerializer

class ProductViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PromotionViewSet(ListModelMixin, RetrieveModelMixin,
                        GenericViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer