from django import forms
from .models import ProfileInfo
from django.contrib.admin import widgets

#form for creating and editing a profile.
class ProfileForm(forms.ModelForm):
    dateOfBirth = forms.DateTimeField(
        label='Date of Birth',
        widget=forms.widgets.DateInput(attrs={'type':'date'}),
    )


    class Meta:
        model= ProfileInfo
        fields = ('firstName', 'lastName', 'inputEmail', 'phoneNumber', 'dateOfBirth','locationCriteria', 'eventCategories')
        labels = {
            'locationCriteria' : 'Location Criteria',
            'firstName' : 'First Name',
            'lastName' : 'Last Name',
            'inputEmail' : 'Email',
            'phoneNumber' : 'Phone Number',
            'eventCategories' : 'Event Categories'

        }
        #fields = '_all_'
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['locationCriteria'].empty_label = "SELECT"                                                                                                                                                       