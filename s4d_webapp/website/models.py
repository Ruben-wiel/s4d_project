from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    # Geeft aan dat de post van de gebruiker moet worden verwijdert indien de gebruiker verwijdert wordt
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reward = models.TextField()
    # Geeft data van wanneer de post GEPOST wordt
    # TIMEZONE IS UTC , MOET NAAR ONZE TIJDZONE (+2 uur)
    date_posted = models.DateTimeField(default=timezone.now)
    # Geeft data van wanneer de post voor het LAATST GEWIJZIGD is
    #last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):  # Deze functie werkt als een methode per post.
        return self.title
