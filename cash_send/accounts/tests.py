from django.test import TestCase , Client
from .models import Country , Accounts , UserRegistrationModel , Profile
from rest_framework import status
from django.utils import timezone


class TestAccounts(TestCase):


    def setUp(self):
        self.country = Country.objects.create(
            country = 'Cameroun',
            code_of_country = '237',
            drapeau = 'vert-rouge-jaune'
        )

        self.accounts = Accounts.objects.create(
            user = {
                'numero_telephone':'657486000',
                'pays':'CMR',
            } ,
            solde = '2500',
            devise = 'EUR'
        )


        self.user = UserRegistrationModel.objects.create(
            numero_telephone = '657486000',
            pays = 'CMR'
        )

        self.profile = Profile.objects.create(
            user = {
                'numero_telephone':'657486000',
                'pays':'CMR',
            } ,

            document_of_personnel_identification = 'carte_identite',
            adress_of_residence = 'Baffoussam',
            region = 'Baffoussam'
        )




         
        
