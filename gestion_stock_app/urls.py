from django.urls import path
from . import views

app_name = "gestion_stock_app"

urlpatterns = [
    path('', views.index, name='index'),  
    path('ajoute/', views.ajoute_stock, name='ajoute_stock'),  
    path('lis/', views.lis_stock, name='list_stock'),  
    path('detay/<int:id>/', views.detay_stock, name='detay_stock'),  
    path('modifye/<int:id>/', views.modifye_stock, name='modifye_stock'),  
    path('efase/<int:id>/', views.efase_stock, name='efase_stock'),  
]
