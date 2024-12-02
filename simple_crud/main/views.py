from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produkt

def index(request):
    return render(request, 'main/dashboard.html')

def products(request):
    produkty = Produkt.objects.all()
    return render(request, 'main/index.html', {'produkty': produkty})

def product_id(request, product_id):
    produkt = get_object_or_404(Produkt, id=product_id)
    return render(request, 'main/show.html', {'produkt': produkt})

def create_product(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        opis = request.POST.get('opis')
        cena = request.POST.get('cena')
        dostepny = request.POST.get('dostepny') == 'on'

        if nazwa and cena:
            Produkt.objects.create(
                nazwa=nazwa,
                opis=opis,
                cena=cena,
                dostepny=dostepny
            )
            messages.success(request, 'Produkt został pomyślnie utworzony!')
            return redirect('wszystkie_produkty')
        else:
            messages.error(request, 'Nie udało się utworzyć produktu. Sprawdź, czy nazwa i cena są wypełnione.')

    return render(request, 'main/new.html')