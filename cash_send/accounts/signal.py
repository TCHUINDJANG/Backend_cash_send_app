from django.db.models .signals import post_save , pre_save , post_delete , pre_delete , m2m_changed
from django.dispatch import receiver
from .models import UserRegistrationModel
from accounts.models import Profile 



#lorke tu cree un utilisateur ca signale dans la table profile directement
@receiver(post_save , sender = UserRegistrationModel)
def create_profile_on_registration(sender , instance , created ,**kwargs):
        user = instance
        if created:
            try:
                Profile.objects.create(user = user)
            except ValueError:
                 isinstance.delete()
