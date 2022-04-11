from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title