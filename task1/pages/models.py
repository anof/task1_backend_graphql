from django.db import models

class Music(models.Model):
    albums = models.TextField(null=True)
    artists = models.TextField(null=True)
    songs = models.TextField(null=True)

