from django.db import models

class Stock(models.Model):
    nom = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    quantite = models.PositiveIntegerField()  
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2) 
    date_ajout = models.DateTimeField(auto_now_add=True)  
    date_mise_a_jour = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.nom} ({self.quantite} disponib)"
