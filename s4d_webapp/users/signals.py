# Dit signaal wordt aangeroepen telkens wanneer er een object is gesaved.
# Dit signaal zorgt ervoor dat een gebruiker na registratie een profiel krijgt (dus niet via de admin-site)
# We willen een 'post_save' signal aanroepen telkens als er een User wordt gesaved.
from django.db.models.signals import post_save
# De verzender wordt aangeroepen:
from django.contrib.auth.models import User
# De ontvanger wordt aangeroepen:
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
