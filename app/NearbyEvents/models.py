from django.db import models

class LocationPreferences(models.Model):
    cafeName = models.CharField(max_length=255)
    EventAddress = models.CharField(max_length=500)
    CafeContact = models.BigIntegerField()
    lat = models.FloatField(('Latitude'), blank=True, null=True)
    lon = models.FloatField(('Longitude'), blank=True, null=True)

    def __str__ (self):
        return self.cafeName