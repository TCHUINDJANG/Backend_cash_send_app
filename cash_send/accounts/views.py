from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from .serialize import AccountsSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 
from rest_framework import status

class AccountviewViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

    def create(self, request, *args, **kwargs):
        account_data = JSONParser().parse(request)
        account_serializer = AccountsSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response({"message": "Ajout du compte utilisateur avec succès"}, status=status.HTTP_201_CREATED)
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

