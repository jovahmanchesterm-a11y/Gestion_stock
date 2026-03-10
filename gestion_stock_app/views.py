from django.shortcuts import render
from . import views


# Create your views here.
def home(request):
    return render(request,'index.html')
# views.py nan aplikasyon gestion_stock_app
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock

def index(request):
    return render(request, './index.html')

def ajoute_stock(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        quantite = request.POST.get('quantite')
        prix_unitaire = request.POST.get('prix_unitaire')
        Stock.objects.create(
            nom=nom,
            quantite=quantite,
            prix_unitaire=prix_unitaire,
        )
        return redirect('gestion_stock_app:list_stock')
    return render(request, 'ajoute_stock.html')

def lis_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'list_stock.html', {'stocks': stocks})

def detay_stock(request, id):
    stock = get_object_or_404(Stock, id=id)
    return render(request, 'detay_stock.html', {'stock': stock})

def modifye_stock(request, id):
    stock = get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        stock.nom = request.POST.get('nom')
        stock.quantite = request.POST.get('quantite')
        stock.prix_unitaire = request.POST.get('prix_unitaire')
        stock.save()
        return redirect('gestion_stock_app:list_stock')
    return render(request, 'modifye_stock.html', {'stock': stock})

def efase_stock(request, id):
    stock = get_object_or_404(Stock, id=id)
    stock.delete()
    return redirect('gestion_stock_app:list_stock')
