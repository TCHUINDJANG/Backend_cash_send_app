from rest_framework.routers import DefaultRouter
from .views import RegisterUserView , LoginUserView ,DeleteUserView, UserProfileView ,PasswordResetResquestView, SendPhoneVerificationCode  , VerifyPhoneNumber , UserDeleteView
from django.urls import path, include 


router = DefaultRouter()
# router.register(r'^accounts/register', AccountviewViewSet, basename='register')




api_urlpatterns = [
    path('accounts/' , include('rest_registration.api.urls')),
    # path('register/', RegisterUserView.as_view(), name='register'),
    # path('login/', LoginUserView.as_view(), name='login'),
    # path('password-reset/', PasswordResetResquestView.as_view(), name='password-reset'),
    # path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('update/', UserUpdateView.as_view(), name='user_update'),
    # path('profile/', UserProfileView.as_view(), name='profile'),  
    # path('send-phone-verification/', SendPhoneVerificationCode.as_view(), name='send-phone-verification'),
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