from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Chambre(models.Model):
    TYPE_CHOICES = [
        ('SIMPLE', 'Chambre Simple'),
        ('DOUBLE', 'Chambre Double'),
        ('SUITE', 'Suite Deluxe'),
    ]
    numero = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='SIMPLE')
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Chambre {self.numero} ({self.get_type_display()})"

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('CONFIRMED', 'Confirmée'),
        ('PENDING', 'En attente'),
        ('CANCELLED', 'Annulée'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reservations')
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name='reservations')
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='PENDING')

    def __str__(self):
        return f"Réservation #{self.id} - {self.client} ({self.chambre.numero})"

class Facture(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='facture')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Facture #{self.id} - {self.montant} DH"

class Reclamation(models.Model):
    STATUT_CHOICES = [
        ('OPEN', 'Ouverte'),
        ('IN_PROGRESS', 'En cours de traitement'),
        ('RESOLVED', 'Résolue'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reclamations')
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='OPEN')

    def __str__(self):
        return f"Réclamation #{self.id} - {self.client}"
