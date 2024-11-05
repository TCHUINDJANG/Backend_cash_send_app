from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model 


UserModel = get_user_model()

class UserRegistrationModelSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self , validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone'],
            email=validated_data['email'],
        )

        return user
    
    class Meta:
        model = UserRegistrationModel
        fields = ('username', 'password' , 'phone_number' , 'email')

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('user', 'solde', 'devise')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'document_of_personnel_identification', 'adress_of_residence', 'region')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name_of_country', 'code_of_country', 'drapeau')