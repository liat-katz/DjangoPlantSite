from django.urls import path #this takes in a url string and calls a function as the response

from . import views #python syntax that says to look in the same folder for a certain file

urlpatterns=[ #list all urls we want to support, and the view function we want to return when that url is called
    #if a request reaches /calatheas, then execute the views.index function
    # path("<plant_type>", views.other_plants),
    path("", views.index, name="index"),
    path("<plant_type>",views.plant_info, name="plant-types"),
    
] #to make the entire project aware of this url config, we need to go to the plantsite/urls.py file

#this is a urls file for the specific app