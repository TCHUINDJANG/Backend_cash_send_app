import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser 


ROLE_CHOICES = [
        ('user', 'Utilisateur'),
        ('admin', 'Administrateur'),
        ('operator', 'Opérateur de transaction'),
    ]

class Base_cash_send(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    date_of_update = models.DateTimeField(auto_created=True)
    date_of_creation = models.DateTimeField(auto_created=True)
    ip_adress =  models.GenericIPAddressField(null=True , blank=True)
	
    class Meta:
        abstract=True


class Country(Base_cash_send):
    name_of_country = models.CharField(max_length=10)
    code_of_country = models.CharField(max_length=50)
    drapeau = models.ImageField(upload_to='flag' , null = True , blank=True)

    class Meta:
            ordering = ['-name_of_country'] 

    def __str__(self):
             return self.name_of_country
    

class UserRegistrationModel(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    country = models.ForeignKey(Country ,on_delete=models.SET_NULL , null=True  , blank=True )
    is_verified_phone = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)
    verification_code = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
   
    class Meta:
            ordering = ['-country'] 

    def __str__(self):
             return self.username
    



class Accounts(Base_cash_send):
    user = models.OneToOneField(UserRegistrationModel, on_delete=models.PROTECT)
    solde = models.PositiveIntegerField(("Solde disponible dans le compte") , default = 0)
    devise = models.CharField(max_length=10)
    
    class Meta:
            ordering = ['-solde'] 

    def __str__(self):
             return self.solde
    

class Profile(Base_cash_send):
    user = models.OneToOneField(UserRegistrationModel, on_delete=models.CASCADE)
    document_of_personnel_identification = models.FileField(upload_to='documents' , null=True , blank=True)
    adress_of_residence = models.CharField(max_length=10 , null=True , blank=True)
    region = models.CharField(max_length=30)
    birth_day = models.DateField(null=True , blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    class Meta:
            ordering = ['-user'] 

    def __str__(self):
             return f"{self.first_name} {self.last_name}"
    



    



