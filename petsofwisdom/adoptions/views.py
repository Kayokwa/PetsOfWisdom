from django.shortcuts import render
from django.http import Http404
from .models import Pets

# Create your views here.
def home(request):
    pets = Pets.objects.all()
    return render(request, 'home.html', 
    {
        'pets': pets,
    })

def pet_detail(request, pet_id):
    try:
        pet = Pets.objects.get(id=pet_id)
    except Pets.DoesNotExist:
        raise Http404 ('Pet not found')
    return render(request, 'pet_detail.html', 
    {
        'pet': pet,
    })