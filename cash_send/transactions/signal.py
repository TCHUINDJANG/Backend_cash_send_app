from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Transaction



@receiver(post_save , sender=Transaction)
def send_transaction_notification(sender, instance, created , **kwargs):
    if not created:   #si la transaction a ete mis a jour
        subject = f'Status de votre transaction {instance.id} change'
        message = f'Votre transaction dun montant de {instance.amount} a change de status a {instance.status}'
        recipient = instance.sender.mail  #on 'envoie la notification a l'expediteur
        send_mail(subject ,message , 'paulnicolas519@gmail.com' , [recipient] )
