from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from cash_send.users.api.views import *
from accounts.views import AccountviewViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("accounts" , AccountviewViewSet)


app_name = "api"
urlpatterns = router.urls
