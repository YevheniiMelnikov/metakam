from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, TagViewSet, BrandViewSet, SupplierViewSet, InventoryViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'tags', TagViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
