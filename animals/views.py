from django.shortcuts import render
from .models import Animal
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def home(request):
    animals = Animal.objects.all()
    cats = Animal.objects.filter(animal='Cat')
    no_of_cats = len(cats)

    paginator1 = Paginator(cats, 10)
    page = request.GET.get('catpage')
    cats = paginator1.get_page(page)

    dogs = Animal.objects.filter(animal='Dog')
    no_of_dogs = len(dogs)
    
    paginator2 = Paginator(dogs, 10)
    page = request.GET.get('dogpage')
    dogs = paginator2.get_page(page)
    
    no_of_animals = len(Animal.objects.all())
    return render(request, 'home.html', {'animals': animals,
                                         'cats': cats,
                                         'dogs':dogs,
                                         'no_of_animals': no_of_animals,
                                         'no_of_cats': no_of_cats,
                                         'no_of_dogs': no_of_dogs})

def detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animals = Animal.objects.all()
    return render(request, 'detail.html', {'animal': animal, 'animals': animals})

def search(request):
    animals = Animal.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        animals = animals.filter(
            Q(name__icontains=search_query) |
            Q(animal__icontains=search_query) |
            Q(gender__iexact=search_query)
        )

    return render(request, 'search.html', {'animals':animals, 'search_query': search_query})
