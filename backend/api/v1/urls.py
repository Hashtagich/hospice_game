from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from api.v1.views.item_views import ResourceViewSet

v1_router = DefaultRouter()
v1_router.register('resources', ResourceViewSet, basename='resources')

urlpatterns = [
    path("", include(v1_router.urls)),
]

urlpatterns += [
    path(
        'schema/',
        SpectacularAPIView.as_view(api_version='api/v1'),
        name='schema'
    ),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
