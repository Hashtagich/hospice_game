from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from .views.user_view import (UserViewSet, LevelUpView, MoneyUpView, PuzzlesUpView, ExperienceUpView, PuzzlesDownView,
                              MoneyDownView)
from .views.npc_view import (DoctorViewSet, UserDoctorViewSet, LevelUpDoctorView, UserPatientViewSet)
from .views.environment_view import (RoomViewSet, FurnitureViewSet, UserRoomViewSet, LevelUpRoomView,
                                     UserFurnitureViewSet)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('doctors', DoctorViewSet, basename='doctors')
v1_router.register('rooms', RoomViewSet, basename='rooms')
v1_router.register('furniture', FurnitureViewSet, basename='furniture')
v1_router.register('user_room', UserRoomViewSet, basename='user-room')
v1_router.register('user_doctor', UserDoctorViewSet, basename='user-doctor')
v1_router.register('user_furniture', UserFurnitureViewSet, basename='user-furniture')
v1_router.register('user_patient', UserPatientViewSet, basename='user-patient')

urlpatterns = [
    path("", include(v1_router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
]

# Users method
urlpatterns += [
    path('level_up/', LevelUpView.as_view(), name='level-up'),
    path('money_up/', MoneyUpView.as_view(), name='money-up'),
    path('money_down/', MoneyDownView.as_view(), name='money-down'),
    path('puzzles_up/', PuzzlesUpView.as_view(), name='puzzles-up'),
    path('puzzles_down/', PuzzlesDownView.as_view(), name='puzzles-down'),
    path('experience_up/', ExperienceUpView.as_view(), name='experience-up'),
]

# Room
urlpatterns += [
    path('level_up_room/<int:user_room_id>/', LevelUpRoomView.as_view(), name='level_up_room'),
]

# Doctor
urlpatterns += [
    path('level_up_doctor/<int:user_doctor_id>/', LevelUpDoctorView.as_view(), name='level_up_doctor'),
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
