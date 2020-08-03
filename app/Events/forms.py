from django import forms
from .models import EventInfo
from django.contrib.admin import widgets

class EventForm(forms.ModelForm):
    EventDate = forms.DateTimeField(
        label='Event Date',
        widget=forms.widgets.DateTimeInput(attrs={'type':'date'}),
    )
    
    class Meta:
        model= EventInfo
        fields = ('EventName', 'EventDescription', 'EventLocation', 'NoofAttendees', 'EventDate')
        #fields = '__all__'
        widgets = {
            'EventDate': forms.DateTimeInput(attrs={'class':'form-control'}),
        }
