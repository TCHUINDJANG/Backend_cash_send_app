from rest_framework import serializers
from models import *

class UserRegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrationModel
        fields = ('numero_telephone', 'pays')

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