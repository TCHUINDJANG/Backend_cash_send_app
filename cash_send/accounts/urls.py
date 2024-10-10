from rest_framework.routers import DefaultRouter
from .views import AccountviewViewSet
from django.urls import path, include 


router = DefaultRouter()
router.register(r'accounts', AccountviewViewSet, basename='account')


urlpatterns = [
    path('', include(router.urls)), 
  # Nouvelle URL pour le comptage
] 