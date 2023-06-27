from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('collections', views.CollectionViewSet)
router.register('collections', views.CollectionDetailViewSet)
router.register('products', views.ProductViewSet)
router.register('promotions', views.PromotionViewSet)

urlpatterns = [
    path('', views.index, name='index')
] + router.urls