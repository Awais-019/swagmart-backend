from django.http import HttpResponse
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Collection
from .serializers import CollectionSerializer

# Create your views here.
def index(request):
    return HttpResponse("Server is up and running!")


class CollectionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer