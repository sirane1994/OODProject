from django.shortcuts import render, HttpResponse, render_to_response
from Profile.models import ProfileInfo
from Events.models import EventInfo
from django.contrib import messages
from django.template import RequestContext
#from social.apps.django_app.default.models import social_auth_usersocialauth
# Create your views here.

# Just to chek if the connect is correct or not
def login(request):
    return HttpResponse('login')
    
# Index page loading.    
def index(request):
    return render(request, 'Login.html')

# Profile display function

def login_post(request):
    InputEmail = request.POST["userEmail"]
    userPassword = request.POST["userPassword"]

    try:
        ProfileInfo_ = ProfileInfo.objects.get(inputEmail=InputEmail, userPassword=userPassword)
        #messages.success(request, 'SUCCESS!')
        session_id = request.session.get('userid',0) 
        request.session['userid'] = ProfileInfo_.id
        id_session = request.session.get('userid')
        id = request.session['userid']
        events = EventInfo.objects.all() 
       
        return render(request, 'Event_Dashbord.html', {'events' : events ,'id': id_session})
        
    except ProfileInfo.DoesNotExist: 
        print("username..")
        messages.error(request, "Username or Password not correct.")
        return render(request, 'Login.html')

#Log Out View function

def logout(request):
    del request.session['userid']
    return render(request, 'Login.html')

