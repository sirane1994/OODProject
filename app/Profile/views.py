from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import ProfileInfo
from django.views import View
from django.views.generic import TemplateView
from .forms import ProfileForm


# Create your views here.
""" def profile_creation(request):
    return render(request, 'Profile_creation.html') """

#Profile creating index page
class Profile_Creation(TemplateView):
    template_name = 'Profile_creation.html'

# Loading the created profile
class Created_Profile(View):
    def created_profile(self, request, inputEmail):
        return render_to_response('Created_Profile.html', {
        'profile' : get_object_or_404(ProfileInfo, inputEmail=inputEmail)
    })


#function for creating the profile and saving it in the database.
def profile_creation_post(request):

    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    inputEmail = request.POST["inputEmail"]
    userPassword = request.POST["userPassword"]
    phoneNumber = request.POST["phoneNumber"]
    dateOfBirth = request.POST["dateOfBirth"]
    locationCriteria = request.POST.getlist("locationCriteria")
    eventCategories = request.POST.getlist("eventCategories")

    profileInfo = ProfileInfo()
    profileInfo.firstName=firstName
    profileInfo.lastName=lastName
    profileInfo.inputEmail=inputEmail
    profileInfo.userPassword=userPassword
    profileInfo.phoneNumber=phoneNumber 
    profileInfo.dateOfBirth=dateOfBirth
    profileInfo.locationCriteria=locationCriteria
    profileInfo.eventCategories=eventCategories
    profileInfo.save()
    
    #reated_profile = Created_Profile()
    #return created_profile.created_profile(request, inputEmail)
    return render(request, "Login.html")
    #return created_profile(request, inputEmail)

""" class Profile_Creation_Post(View):

    def profile_creation_post(self, request):
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        inputEmail = request.POST["inputEmail"]
        userPassword = request.POST["userPassword"]
        phoneNumber = request.POST["phoneNumber"]
        dateOfBirth = request.POST["dateOfBirth"]
        locationCriteria = request.POST.getlist("locationCriteria")
        eventCategories = request.POST.getlist("eventCategories")

        profileInfo = ProfileInfo()
        profileInfo.firstName=firstName
        profileInfo.lastName=lastName
        profileInfo.inputEmail=inputEmail
        profileInfo.userPassword=userPassword
        profileInfo.phoneNumber=phoneNumber 
        profileInfo.dateOfBirth=dateOfBirth
        profileInfo.locationCriteria=locationCriteria
        profileInfo.eventCategories=eventCategories
        profileInfo.save()

        created_profile = Created_Profile()
        return created_profile.created_profile(request, inputEmail) """


""" def created_profile(request, inputEmail): 
    return render_to_response('Created_Profile.html', {
        'profile' : get_object_or_404(ProfileInfo, inputEmail=inputEmail)
    }) """

#Edit and crete event code same for both the pages.

def editProfile_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = ProfileForm()
        else:
            profiles = ProfileInfo.objects.get(pk=id)
            form = ProfileForm(instance=profiles)
        return render(request, "Edit_Profile.html", {'form':form})
    else:
        if id==0:
            form = ProfileForm(request.POST)
        else:
            profiles = ProfileInfo.objects.get(pk=id)
            form = ProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()
            profiles = ProfileInfo.objects.get(pk=id)
        return redirect('/Dashboard')
