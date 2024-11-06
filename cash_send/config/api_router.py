from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework import views

# from cash_send.users.api.views import *


router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)
# router.register("accounts" , views.)


app_name = "api"
urlpatterns = router.urls
