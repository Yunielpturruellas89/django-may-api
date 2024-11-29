from django.urls import path,include
from rest_framework import routers
from .views import RatingViewSet

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet) #  'hymns' es el prefijo de la URL
urlpatterns = [
    path('', include(router.urls)),
]