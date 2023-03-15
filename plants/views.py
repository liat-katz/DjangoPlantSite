from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string


plant_types={
    'philodendrons': "These are good for LECA!",
    'calatheas': 'These love moisture!',
    'hoyas': 'These are slow growers!',
    'peperomias': 'These don\'t need a lot of water!',
    'anthuriums': 'These love humidity!',
    'bromeliads': None
}
# Create your views here.

def index(request):
    the_plant_types=list(plant_types.keys())
    
    return render(request, "plant_types/index.html", {"the_plant_types":the_plant_types})



#this will be executed automatically by django
#this is the exchange of the request-response cycle

def plant_info(request, plant_type):
    try:
        plant_text=plant_types[plant_type]
        return render(request, "plant_types/plant_types.html", {"text": plant_text,
                                                                "plant_type_name":plant_type})
    except:
        return HttpResponseNotFound("<h1>This plant family isn't registered yet!</h1>")