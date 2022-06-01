from django.shortcuts import render, get_object_or_404
from .models import Accommodation, ListOfCountries

def main(request):
    return render(request, 'mainapp/index.html')



def accommodations(request):
    title = "accommadation"

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'mainapp/accomodations.html', content)


def accomodation(request, pk):
    title = 'products'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'mainapp/accomodation_details.html', content)
