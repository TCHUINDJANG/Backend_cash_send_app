from django.db import models
from .models import Base_cash_send
from models import *


choices = (('EN_COURS' , 'en_cours') , ('TERMINE' , 'termine') ,('ECHOUE' , 'echoue') )
devices = (('EURO' , 'euro') , ('FCFA' , 'fcfa') , ('DOLLARS'  , 'dollars'))

class Transaction (Base_cash_send):
    sender_account_id = models.EmailField(_('sender'),max_length=100)
    receiver_account_id  = models.CharField(_('receiver'), max_length=100)
    price = models.IntegerField(_("montant"), max_length=15)
    devise = models.TextChoices(devices)
    statut = models.TextChoices(choices)
    user = models.ManyToManyField(UserRegistrationModel ,on_delete=models.CASCADE)
    
    class Meta:
            ordering = ['-date_transaction'] 

    def __str__(self):
             return self.montant
    


class TransactionHistory (Base_cash_send):
    transaction_id = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    sender_account_id = models.EmailField(_('sender'),max_length=100)
    receiver_account_id  = models.CharField(_('receiver'), max_length=100)
    statut_new_history_transaction= models.TextChoices(choices)
    statut_last_history_transaction= models.TextChoices(choices)
    
    class Meta:
            ordering = ['-statut_last_history_transaction'] 

    def __str__(self):
             return self.montant


class Notification (Base_cash_send):
    transaction_id = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    message = models.TextField(max_length=300)
    as_read = models.BooleanField(default=False)
    
    class Meta:
            ordering = ['-transaction_id'] 

    def __str__(self):
             return self.transaction_id

