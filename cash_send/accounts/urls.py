from rest_framework.routers import DefaultRouter
from .views import AccountviewViewSet
from django.urls import path, include 


router = DefaultRouter()
router.register(r'^accounts/register', AccountviewViewSet, basename='register')


urlpatterns = [
    path('', include(router.urls)), 
  # Nouvelle URL pour le comptage
] 