from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewset


router = DefaultRouter()

router.register(r'products', ProductViewset , 'product')


urlpatterns = [
    path('', include(router.urls)),
]