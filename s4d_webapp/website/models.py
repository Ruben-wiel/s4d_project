from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    titel = models.CharField(max_length=100)
    # Geeft aan dat de post van de gebruiker moet worden verwijdert indien de gebruiker verwijdert wordt
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    beschrijving = models.TextField(max_length=500)
    beloning = models.TextField(max_length=500)
    #phone = models.TextField(max_length=100)
    # Geeft data van wanneer de post GEPOST wordt
    # TIMEZONE IS UTC , MOET NAAR ONZE TIJDZONE (+2 uur)
    date_posted = models.DateTimeField(default=timezone.now)
    # Geeft data van wanneer de post voor het LAATST GEWIJZIGD is
    #last_modified = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

    #FAVORITEN TOEVOEGEN AAN JE ACCOUNT (JENTE)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):  # Deze functie werkt als een methode per post.
        return self.titel

    def get_absolute_url(self):
        # deze reverse laat de gebruiker na het aanmaken van de post naar de detail pagina gaan.
        # KAN AANGEPAST WORDEN NAAR ANDERE PAGINA!!!

        # set an atribute in the create view called succes URL en die doorsturen naar de homepage
        # wordt in part 10 uitgelegd bij 30:30.
        return reverse('post-detail', kwargs={'pk': self.pk})

        # redirect will redirect you to a specific URL
        # reverse will return the full URL to that URL as a string
