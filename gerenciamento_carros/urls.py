from django.contrib import admin
from django.urls import path, include
from carros.views import CarrosViewSet, MarcaViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Gerenciamento de Carros",
      default_version='v1',
      description="API de gerenciamento de carros",
      terms_of_service="#",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('carros', CarrosViewSet, basename='Carros')
router.register('marcas', MarcaViewSet, basename='Marcas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
