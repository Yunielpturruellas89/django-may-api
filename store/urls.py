from django.urls import path,include
from rest_framework import routers
from .views import ProductViewSet
from ratings.urls import urlpatterns as ratings_urls
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet) #  'hymns' es el prefijo de la URL
urlpatterns = [
    path('', include(router.urls)),
    path('', include(ratings_urls)), # Include ratings URLs here
]