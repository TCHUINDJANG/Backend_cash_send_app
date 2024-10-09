from django.db import models




class Transaction ():
    sender_account_id = models.EmailField(_('sender'),max_length=100)
    receiver_account_id  = models.CharField(_('receiver'), max_length=100)
    montant = models.IntegerField(_("montant"), max_length=15)
    devise = models.CharField()
    prenom = models.CharField()
    date_transaction = models.Choices()
    date_creation = models.DateTimeField()
    statut = models.TextChoices()
    



    class Meta:
            ordering = ['-date_transaction'] 

#permet de representer notre instance sous forme de chaine de caractere
    def __str__(self):
             return self.montant

