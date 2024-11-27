from django.urls import path,include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet) #  'hymns' es el prefijo de la URL
urlpatterns = [
    path('', include(router.urls)),
]