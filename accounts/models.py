from django.db import models
from .models import  UserRegistrationModel




class Accounts(models.Model):
    user = models.ForeignKey(UserRegistrationModel, on_delete=models.CASCADE)
    solde = models.PositiveIntegerField(_("Solde disponible dans le compte"))
    date_creation = models.DateTimeField(auto_now_add=True)
    devise = models.CharField(max_length=10)
    
    class Meta:
            ordering = ['-date_creation'] 

#permet de representer notre instance sous forme de chaine de caractere
    def __str__(self):
             return self.solde


