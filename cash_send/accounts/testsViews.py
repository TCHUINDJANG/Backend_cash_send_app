from django.test import TestCase , Client
from django.urls import reverse
from .models import Country , Accounts , UserRegistrationModel 

class TestCaseAccountsView(TestCase):

    def setup(self):

        self.client = Client()
        self.user_data = {
            'username':'david',
            'password':'1234',
            'numero_telephone':'65786000',
            'email':'david@gmail.com'
        }

        self.user = UserRegistrationModel.objects.create_user(**self.user_data)


    def test_register_view(self):

        url = reverse('accounts/register')

        response = self.client.get(url)

        self.assertEqual(response.status_code , 200)
#envoyons les donnes sur cette vue donne demande a l'utilisateur
        data = {
            'email':'david@gmail.com',
            'password':'1234',
            'numero_telephone':'234456098',
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code , 200)
        self.assertTrue(UserRegistrationModel.objects.filter(username='test1').exists())



    def test_login_view(self):

        url = reverse('Account:login')

        response = self.client.get(url)

        self.assertEqual(response.status_code , 200)
#recuperons l'utilisateur
        user = UserRegistrationModel.objects.get(email='paulnicolas519@gmail.com')

        response = self.client.post(url , 
                                    {'phonenumber':'657486000',
                                    'password' : '123456',
                                    'email' : 'paulnicolas519@gmail.com'})
        
        self.assertEqual(response.status_code , 200)
        self.assertTrue(user.is_authenticated())



    def test_logout_view(self):
#j'essaie de loger l'utilisateur
        self.client.login(email = self.user_data['email'] ,password = self.user_data['password'])
#recuperons l'URL

        url = reverse('account:logout')

        response = self.client.get(url)

#kan on se deconecte ca nous renvoit vers la page de login
        self.assertEqual(response.status_code , 302)
#recuperons l'utilisateur
        user = UserRegistrationModel.objects.get(email=self.user_data['email'])
#verifions que l'utilisateur n'est plus connecte
        self.assertFalse(user.is_authenticated)


    def test_reset_password(self):
        pass