from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from .views.user_view import (UserViewSet, LevelUpView, MoneyUpView, PuzzlesUpView, ExperienceUpView, PuzzlesDownView,
                              MoneyDownView)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path("", include(v1_router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
]

urlpatterns += [
    path('level_up/', LevelUpView.as_view(), name='level-up'),
    path('money_up/', MoneyUpView.as_view(), name='money-up'),
    path('money_down/', MoneyDownView.as_view(), name='money-down'),
    path('puzzles_up/', PuzzlesUpView.as_view(), name='puzzles-up'),
    path('puzzles_down/', PuzzlesDownView.as_view(), name='puzzles-down'),
    path('experience_up/', ExperienceUpView.as_view(), name='experience-up'),
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
