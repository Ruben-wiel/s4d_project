from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # default = true -> dan mag het ChafField leeg blijven. Indien False dan MOET er iets in staan.

    biography = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    # Hier moet nog meer belangrijke profiel informatie komen

    def __str__(self):
        return f'{self.user.username} Profile'

    #Resized images voor de profielfoto, zodat er geen onnodige grote fotos geladen hoeven worden.
    #Na tutorial 9 problemen met registreren, gefixt met *args & **kwargs toevoeging op lijn 24 en 25 m.b.v. volgende link:
    #https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) #super runned de savemethod van de parent class

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
