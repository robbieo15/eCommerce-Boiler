from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename="category")
router.register('products', views.ProductViewSet, basename="product")

urlpatterns = [  
    path('api/', include(router.urls)),
    path("",views.home)
]