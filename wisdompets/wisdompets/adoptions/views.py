from django.shortcuts import render
from django.http import Http404

from  .models import Pet

def home(req):
    pets = Pet.objects.all()
    
    return render(req, 'home.html', {
        'pets':pets,
    })

def pet_detail(req, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(req, 'pet_detail.html', {
        'pet': pet, 
    })