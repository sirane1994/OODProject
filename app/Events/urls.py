from django.conf.urls import include, url
from django.urls import path
from Events import views as Events_views

urlpatterns = [
    #path('created_event/,', Events_views.Created_Event.as_view()),
    url(r'^Event/$', Events_views.Event_Creation.as_view()),
    url(r'^Dashboard/$', Events_views.Event_List_View.as_view()),
    url(r'^event_creation_post/$', Events_views.event_creation_post),
    url(r"^created_event/(.*)$", Events_views.Created_Event.as_view()),
    url(r"^join_event/(.*)$", Events_views.Join_Event.as_view()),
    url(r"^delete_event/(.*)$", Events_views.Delete_Event.as_view()),

    url(r'^new/$', Events_views.Event_List_View_form.as_view()),
    url(r"^edit_event/$", Events_views.editEvent_form),
    url(r"^NewCreatedEvent/(?P<id>\d+)$", Events_views.editEvent_form),
    
    url(r"^edit_event_post/(.*)$", Events_views.edit_event_post),
]