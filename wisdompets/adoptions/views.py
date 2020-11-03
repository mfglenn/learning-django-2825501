from django.shortcuts import render
from django.http import Http404

#Import Models for Queries
from .models import Pet

# Return the Home View
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
    })

# Return the Pet Detail
def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')

    return render(request, 'pet_detail.html', {
        'pet': pet,
    })