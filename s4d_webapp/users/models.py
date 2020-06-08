from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # Default = True -> dan mag het ChafField leeg blijven. Indien False dan MOET er iets in staan.
    # Hier moet nog meer belangrijke profiel informatie komen.

    def __str__(self):
        return f'{self.user.username} Profile'

    # Resized images voor de profielfoto, zodat er geen onnodige grote fotos geladen hoeven worden.
    # Na tutorial 9 problemen met registreren, gefixt met *args & **kwargs toevoeging op lijn 24 en 25 m.b.v. volgende link:
    # https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert

    # Deze functie zorgt voor het resizen van de profielfoto's

    # def save(self, *args, **kwargs):
    #     # super runned de savemethod van de parent class
    #     # Eventueel arguments van super weg --> (Profile, self) weghalen
    #     super(Profile, self).save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adres = models.CharField(max_length=30, blank=False,
                             help_text="Straat + huisnummer")
    telefoon = models.CharField(
        max_length=12, blank=True, help_text="Vul 06-, +316- of Huis- nummer in")

    def __str__(self):
        return self.user.username
