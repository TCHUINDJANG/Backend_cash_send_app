from django.db import models
from django.contrib.auth.models import AbstractUser , User



class UserRegistrationModel(AbstractUser):
    email = models.EmailField(_('email'),max_length=100)
    password = models.CharField(_('password'), max_length=100)
    numero_telephone = models.IntegerField(_("numero telephone"), max_length=15)
    nom = models.CharField()
    prenom = models.CharField()
    pays = models.Choices()
    date_creation = models.DateTimeField()
    date_derniere_connexion = models.DateTimeField()
    is_actif = models.BooleanField(default=False)




    class Meta:
            ordering = ['-date_creation'] 

#permet de representer notre instance sous forme de chaine de caractere
    def __str__(self):
             return self.numero_telephone
