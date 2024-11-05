from django.test import TestCase , Client
from .models import Country , Accounts , UserRegistrationModel , Profile
from rest_framework import status
from django.utils import timezone


class TestCaseAccounts(TestCase):


    def setUp(self):

        self.data = {
            'username':'david',
            'numero_telephone':'657486000',
            'password':'1234',
            'email':'paulnicolas519@gmail.com'
        }

        self.user = UserRegistrationModel.objects.create_user(**self.data)

        self.country = Country.objects.create(
            name_of_country  = 'Cameroun',
            code_of_country = '237',
        )

        self.accounts = Accounts.objects.create(
            user = self.user,
            solde = '2500',
            devise = 'EUR'
        )
           

        self.profile = Profile.objects.create(
            user = self.user,
            email = self.user.email
        )



    def test_profile(self):
        self.assertEqual(self.profile.user , self.user)

    def test_profile_email(self):
        self.assertEqual(self.profile.email , self.user.email )
        self.data['email'] = 'david@gmail.com'
        self.assertNotEqual(self.profile.email , self.data['email'])


    def test_user_country(self):
        self.assertEqual(self.user.country , self.country)


       




         
        
