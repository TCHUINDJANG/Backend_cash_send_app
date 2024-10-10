import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser 



class Base_cash_send(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    date_of_update = models.DateTimeField(auto_created=True)
    date_of_creation = models.DateTimeField(auto_created=True)
    ip_adress =  models.IPAddressField(null=True , blank=True)
	
    class Meta:
        abstract=True


class Country(Base_cash_send):
    name_of_country = models.CharField(max_length=10)
    code_of_country = models.CharField(max_length=50)
    drapeau = models.CharField()

    class Meta:
            ordering = ['-name_of_country'] 

    def __str__(self):
             return self.name_of_country
    

class UserRegistrationModel(AbstractUser):
    numero_telephone = models.IntegerField(_("numero telephone"), max_length=15)
    pays = models.ManyToManyField(Country ,on_delete=models.CASCADE )
   
    class Meta:
            ordering = ['-pays'] 

    def __str__(self):
             return self.numero_telephone
    



class Accounts(Base_cash_send):
    user = models.OneToOneField(UserRegistrationModel, on_delete=models.CASCADE)
    solde = models.PositiveIntegerField(_("Solde disponible dans le compte"))
    devise = models.CharField(max_length=10)
    
    class Meta:
            ordering = ['-date_creation'] 

    def __str__(self):
             return self.solde
    

class Profile(Base_cash_send):
    user = models.OneToOneField(UserRegistrationModel, on_delete=models.CASCADE)
    document_of_personnel_identification = models.TextField()
    adress_of_residence = models.CharField(max_length=10)
    region = models.CharField(max_length=30)

    class Meta:
            ordering = ['-user'] 

    def __str__(self):
             return self.user
    




    



