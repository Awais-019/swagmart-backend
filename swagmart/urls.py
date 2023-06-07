from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('collections', views.CollectionViewSet)

urlpatterns = [
    path('', views.index, name='index')
] + router.urls