from django.contrib import admin
from .models import Client, Chambre, Reservation, Facture, Reclamation

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'email')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('numero', 'type', 'prix')
    list_filter = ('type',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'chambre', 'date_debut', 'date_fin', 'statut')
    list_filter = ('statut', 'date_debut')

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'montant', 'date')

@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'statut')
    list_filter = ('statut',)
