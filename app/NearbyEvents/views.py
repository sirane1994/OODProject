from django.shortcuts import render
from mapbox import Directions
from .models import LocationPreferences
from Events.models import EventInfo
from django.core.serializers import serialize

# Create your views here.
# TODO: move Token to settings.py file

def default_maps(request):
    eventinfo = EventInfo.objects.all().values_list('EventLocation', flat=True)
    
    locationPreferences = LocationPreferences()
    locations = serialize('json', LocationPreferences.objects.filter(id__in=eventinfo))


    
    mapbox_access_token = 'pk.eyJ1IjoicmltYXNoYWg5NTk1IiwiYSI6ImNrNDg2ODZldjEyZzYzZW5uc3R2amthdzkifQ.nO-Z3ySyMnhhTlEeuBxYag'
	
    return render(request, 'NearbyEvents.html', {'mapbox_access_token':mapbox_access_token, 'locations' : locations })