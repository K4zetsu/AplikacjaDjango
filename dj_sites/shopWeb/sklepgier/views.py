from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *


def price(request):
    search_query = request.GET.get('q','')
    if search_query:
        ofertf = lol.objects.filter(name__icontains = search_query)
        if ofertf:
            print('ok')
        else:
           ofertf = lol.objects.filter(category__icontains = search_query)
    else:
        ofertf = lol.objects.all()
    return render(request, 'sklepg/cennik.html',{'ofertsf':ofertf})

def o_nas(request):
    return render(request, 'sklepg/o_nas.html')

def main_p(request):
    return render(request, 'sklepg/strona_glowna.html')

def kontakt(request):
    return render(request, 'sklepg/kontakt.html')

def faq(request):
    return render(request, 'sklepg/faq.html')













