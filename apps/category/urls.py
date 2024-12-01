from django.urls import path,include
from rest_framework import routers
from .views import CategoryViewSet, ListCategoryView

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet) #  'hymns' es el prefijo de la URL
urlpatterns = [
    path('', include(router.urls)),
    path('list', ListCategoryView.as_view())
]