from django.db import models
from accounts.models import Base_cash_send

from django.contrib.auth import get_user_model 



User = get_user_model()
# from .models import UserRegistrationModel


status = (('EN_COURS' , 'en_cours') , ('TERMINE' , 'termine') ,('ECHOUE' , 'echoue') )
devices = (('EURO' , 'euro') , ('FCFA' , 'fcfa') , ('DOLLARS'  , 'dollars') , ('ROUBLE', 'RUB'))


class Transaction (Base_cash_send):
    sender = models.EmailField(User,max_length=100)
    receiver   = models.CharField(User, max_length=100)
    amount  = models.IntegerField(("montant"))
    devise = models.CharField(choices=devices)
    statut = models.CharField(choices = status)
    user = models.ManyToManyField(User)
        #  transaction_date = models.DateTimeField(auto_now_add=True)
        # currency_to = models.ForeignKey(Devise, related_name='currency_to', on_delete=models.CASCADE)
        # currency_from = models.ForeignKey(Currency, related_name='currency_from', on_delete=models.CASCADE)
        # taux_exchange = models.DecimalField(max_digits=10, decimal_places=4)


    
    class Meta:
            ordering = ['-date_of_creation'] 

    def __str__(self):
             return f"Transaction from {self.sender.username} to {self.receiver.username}"
    


class TransactionHistory (Base_cash_send):
    transaction_id = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    sender_account_id = models.EmailField(('sender'),max_length=100)
    receiver_account_id  = models.CharField(('receiver'), max_length=100)
    statut_new_history_transaction= models.CharField(choices=status)
    statut_last_history_transaction= models.CharField(choices=status)
    
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





class Devise (Base_cash_send):
    code = models.CharField(choices=devices)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)  # Taux de change
    last_updated = models.DateTimeField(auto_now=True)  # Date de la dernière mise à jour
    class Meta:
            ordering = ['-code'] 

    def __str__(self):
             return self.code
             


