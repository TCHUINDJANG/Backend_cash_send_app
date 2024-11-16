from django.db import models
from accounts.models import Base_cash_send

from django.contrib.auth import get_user_model 



User = get_user_model()
# from .models import UserRegistrationModel


status = (('EN_COURS' , 'en_cours') , ('TERMINE' , 'termine') ,('ECHOUE' , 'echoue'))
devices = (('EURO' , 'euro') , ('FCFA' , 'fcfa') , ('DOLLARS'  , 'dollars') , ('ROUBLE', 'RUB'))


class Transaction (Base_cash_send):
    sender = models.ForeignKey(User, on_delete= models.CASCADE , related_name='send_transaction')
    receiver   = models.ForeignKey(User, on_delete= models.CASCADE , related_name='send_transactions')
    amount  = models.IntegerField(("montant"))
#     devise = models.CharField(choices=devices)
#     statut = models.CharField(choices = status)
    description = models.CharField(max_length=255 , blank=True , null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
       

    
    class Meta:
            ordering = ['-date_of_creation'] 

    def __str__(self):
             return f"Transaction from {self.sender.username} to {self.receiver.username}"
    


class TransactionHistory (Base_cash_send):
    transaction_id = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    sender_account_id = models.EmailField(('sender'),max_length=100)
    receiver_account_id  = models.CharField(('receiver'), max_length=100)
#     statut_new_history_transaction= models.CharField(choices=status)
#     statut_last_history_transaction= models.CharField(choices=status)
    
    class Meta:
            ordering = ['-sender_account_id'] 

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





# class Devise (Base_cash_send):
#     base_currency = models.CharField(default='XAF')
#     target_currency = models.CharField(default='RUB')  # Taux de change
#     last_updated = models.DateTimeField(auto_now=True)  # Date de la dernière mise à jour
#     rate= models.DecimalField(max_digits=5 , decimal_places=4)
#     class Meta:
#             ordering = ['-base_currency'] 

#     def __str__(self):
#         return f'{self.base_currency} to {self.target_currency} rate: {self.rate}'
             


