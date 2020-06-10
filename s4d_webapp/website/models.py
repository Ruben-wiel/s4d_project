from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import UserProfile


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Klusjes', 'Klusjes'),
        ('Uitlaatservice', 'Uitlaatservice'),
        ('Boodschappen', 'Boodschappen'),
        ('Overig', 'Overig')
    )

    def __str__(self):
        return self.CATEGORY_CHOICES


class Post(models.Model):
    titel = models.CharField(max_length=100)
    # Geeft aan dat de post van de gebruiker moet worden verwijdert indien de gebruiker verwijdert wordt.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    beschrijving = models.TextField(max_length=500)
    beloning = models.TextField(max_length=500)
    categorie = models.TextField(
        default=True, choices=Category.CATEGORY_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)

    locatie = UserProfile.locatie

    def __str__(self):  # Deze functie werkt als een methode per post.
        return self.titel

    def get_absolute_url(self):
        # Deze reverse laat de gebruiker na het aanmaken van de post naar de detail pagina gaan.
        return reverse('post-detail', kwargs={'pk': self.pk})

        # redirect will redirect you to a specific URL
        # reverse will return the full URL to that URL as a string
