from typing import Type
from django.shortcuts import render , redirect
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from .models import * 
from .serialize import AccountsSerializer , UserRegistrationModelSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages 
from django.core.mail  import send_mail , EmailMessage
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_registration.api.views.reset_password import reset_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_registration.api.views.register import RegisterSigner
from rest_registration.api.views.login import login
from rest_registration.api.views.change_password import change_password
from rest_registration.api.views.profile import profile
from rest_registration.api.views.register_email import register_email
from rest_registration.api.views import register
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serialize import ProfileSerializer
import random
from twilio.rest import Client
from django.conf import settings
from rest_registration.api.views.profile import ProfileView
from rest_registration.api.views.register import RegisterView
from rest_registration.api.views.login import LoginView
from .Permissions import AuthorProfilePermission



class RegisterUserView(RegisterView):
    
     def get_serializer_class(self) -> type[Serializer]:
          return super().get_serializer_class()
     
     
class LoginUserView(LoginView):

     def get_serializer_class(self) -> Serializer:
          return super().get_serializer_class()



class getAllProfileView(ProfileView):
     permission_classes = [IsAuthenticated , AuthorProfilePermission]

     def get_serializer_class(self) -> Serializer:
          return super().get_serializer_class()   


class updateProfileView(ProfileView):
     permission_classes = [IsAuthenticated , AuthorProfilePermission]

     def get_serializer_class(self) -> Serializer:
          return super().get_serializer_class()   

    

class deleteProfileView(ProfileView):
     permission_classes = [IsAuthenticated , AuthorProfilePermission]

     def get_serializer_class(self) -> Serializer:
          return super().get_serializer_class()   

    

class getByIdProfileView(ProfileView):
     permission_classes = [IsAuthenticated , AuthorProfilePermission]

     def get_serializer_class(self) -> Serializer:
          return super().get_serializer_class()   

    



# class SendPhoneVerificationCode(APIView):
#     def post(self , request):
#         phone_number = request.data.get('phone_number')
#         if not phone_number:
#             return Response({"detail": "Le numéro de téléphone est requis."}, status=status.HTTP_400_BAD_REQUEST)

#         user = UserRegistrationModel.objects.filter(phone=phone_number).first()
#         if not user:
#             return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)
        
#         # Générer un code de vérification à 6 chiffres
#         verification_code = random.randint(100000, 999999)
#         # Utilisation de Twilio pour envoyer le SMS

#         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#         message = client.messages.create(
#             body=f"Votre code de verification est : {verification_code}",
#             from_=settings.TWILIO_PHONE_NUMBER,
#             to=phone_number
#         )

#         # Sauvegarde du code dans la base de données ou dans un cache temporaire
#         # Il est conseillé de stocker ce code et de le valider dans une autre vue

#         user.verification_code = verification_code
#         user.save()
#         return Response({"detail": "Code de vérification envoyé."}, status=status.HTTP_200_OK)
    

# class VerifyPhoneNumber(APIView):
#     def post(self , request):
#         phone_number = request.data.get("phone_number")
#         verification_code = request.data.get("verification_code")


#         user = UserRegistrationModel.objects.filter(phone=phone_number).first()
#         if not user:
#             return Response({"detail": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)
#         # Vérifier le code de vérification
#         if str(user.verification_code) != (verification_code):
#             return Response({"detail": "Code de vérification invalide."}, status=status.HTTP_400_BAD_REQUEST)

#         # Mettre à jour le statut de l'utilisateur

#         user.is_verified_phone = True
#         user.save()
#         return Response({"detail": "Numéro de téléphone vérifié avec succès."}, status=status.HTTP_200_OK)




# class PasswordResetResquestView(APIView):
#     permission_classes = [AllowAny]


#     def post(self , request):
#         email = request.data.get('email')
#         if not email:
#             return Response({"detail": "L'email est requis."}, status=400)
#         user = UserRegistrationModel.objects.filter(email=email).first()
#         if not user:
#             return Response({"detail": "Utilisateur non trouvé."}, status=404)
#         token = default_token_generator.make_token(user)
#         uid = urlsafe_base64_encode(str(user.pk).encode())


#          # Crée le lien de réinitialisation
#         reset_link = f'http://tonsite.com/reset-password/{uid}/{token}/'



#         # Envoie l'email
#         send_mail(
#             'Réinitialisation du mot de passe',
#             f'Cliquez sur ce lien pour réinitialiser votre mot de passe: {reset_link}',
#             'noreply@tonsite.com',
#             [email],
#             fail_silently=False,
#         )

#         return Response({"detail": "Un email avec les instructions a été envoyé."}, status=200)
    


# class DeleteUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self , request):
#         user = request.user
#         user.delete()
#         return Response({"detail": "Utilisateur supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)













           




