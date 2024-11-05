from django.shortcuts import render , redirect
from rest_framework import viewsets
from .models import * 
from .serialize import AccountsSerializer , UserRegistrationModelSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages 
from accounts import settings
from django.core.mail  import send_mail , EmailMessage
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def api_view_register(request , pk=None, *args, **kwargs):
    if request.method == "POST":
        data = request.data
        serializer = UserRegistrationModelSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            lastname = serializer.validated_data.get('lastname')
            password = serializer.validated_data.get('password')
            password2 = serializer.validated_data.get('password')
            phone_number = serializer.validated_data.get('phone_number')
            email = serializer.validated_data.get('email')
        if UserRegistrationModel.objects.filter(username=username):
            messages.error(request , "ce nom a deja ete utilise pour creer un compte")
            return redirect('register')
        if UserRegistrationModel.objects.filter(email =email):
            messages.error(request , "Cet email possede deja un compte")
        if not username.isalnum():
            messages.error(request , "Le nom doit etre alphanumerique")
            return redirect('register')
        if password != password2:
            messages.error(request , "Les mots de passe ne sont pas egaux")
        user_create = UserRegistrationModel.objects.create(username ,lastname, password, phone_number , email)
        user_create.lastname = lastname
        user_create.phone_number = phone_number
        user_create.email = email
        user_create.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    subject = "Bienvenu chez SEND CASH MONEY"
    message = "Bienvenue" + user_create.username + "" + user_create.lastname + "/n Nus sommes heureux de vous recevoir"
    from_email = settings.EMAIL_HOST_USER
    to_list = [user_create.email]
    send_mail(subject , message , from_email , to_list  , fail_silently=False)
    

    return render(request , '')
