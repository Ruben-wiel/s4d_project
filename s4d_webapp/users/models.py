from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    # default = true -> dan mag het ChafField leeg blijven. Indien False dan MOET er iets in staan.

    biography = models.CharField(default=True, max_length=250)
    location = models.CharField(default=True, max_length=50)
    phone = models.CharField(default=True, max_length=13)
    # posts =
    # Hier moet nog meer belangrijke profiel informatie komen

    def __str__(self):
        return f'{self.user.username} Profile'

    #Resized images voor de profielfoto, zodat er geen onnodige grote fotos geladen hoeven worden.
    def save(self):
        super().save() #super runned de savemethod van de parent class

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
