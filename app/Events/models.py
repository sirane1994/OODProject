from django.db import models
from django.urls import reverse
from Profile.models import ProfileInfo
from NearbyEvents.models import LocationPreferences



class EventInfo(models.Model):
    EventName = models.CharField(max_length = 200)
    EventDescription = models.CharField(max_length = 200)
    EventLocation = models.ForeignKey(LocationPreferences,db_column='EventLocation', on_delete=models.CASCADE)
    NoofAttendees = models.PositiveSmallIntegerField(default=0,null=True)
    EventDate = models.DateTimeField(blank=True, null=True)
    OwnerId = models.PositiveSmallIntegerField(default=0,null=True)
    Attendee = models.ManyToManyField(ProfileInfo, blank= True)
    IsInitialized = models.BooleanField(default=False)

def __str__(self):
    return self.EventName

    
    
   