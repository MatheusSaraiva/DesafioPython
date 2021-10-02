from django.contrib import admin
from django.urls import path, include
from carros.views import CarrosViewSet, MarcaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('carros', CarrosViewSet, basename='Carros')
router.register('marcas', MarcaViewSet, basename='Marcas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
