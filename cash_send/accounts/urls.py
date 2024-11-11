from rest_framework.routers import DefaultRouter
from .views import RegisterUserView , LoginUserView ,updateProfileView , deleteProfileView ,getByIdProfileView, getAllProfileView , VerifyPhoneNumber , UserDeleteView
from django.urls import path, include 


router = DefaultRouter()
# router.register(r'^accounts/register', AccountviewViewSet, basename='register')

 from  rest_registration.api.views import  change_password 
 


api_urlpatterns = [
    # path('accounts/' , include('rest_registration.api.urls')),
    # path('register/', RegisterUserView.as_view(), name='register'),
    # path('login/', LoginUserView.as_view(), name='login'),
    # path('password-reset/', PasswordResetResquestView.as_view(), name='password-reset'),
    path('accounts/login', LoginUserView.as_view(), name='login'),
    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/', getAllProfileView.as_view(), name='profile'),  
    path('accounts/profile/<int:pk>/', updateProfileView.as_view(), name='update-profile'),
    path('accounts/profile/<int:pk>/', getByIdProfileView.as_view(), name='get-profile'),  
    path('accounts/profile/<int:pk>/', deleteProfileView.as_view(), name='delete-profile'),

    # path('verify-phone/', VerifyPhoneNumber.as_view(), name='verify-phone'),
    # path('delete/', DeleteUserView.as_view(), name='delete-user'),
 
]

# urlpatterns += [
#     path('', include(router.urls)), 
#     path('api/v1/', include(api_urlpatterns)),
# ]



# REST_REGISTRATION = {
#     'REGISTER_VERIFICATION_URL': 'https://frontend-host/verify-user/',
#     'RESET_PASSWORD_VERIFICATION_URL': 'https://frontend-host/reset-password/',
#     'REGISTER_EMAIL_VERIFICATION_URL': 'https://frontend-host/verify-email/',

#     'VERIFICATION_FROM_EMAIL': 'paulnicolas519@gmail.com',
# }