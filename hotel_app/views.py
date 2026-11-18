from django.shortcuts import render
from django.http import JsonResponse
from .models import Chambre, Reservation, Client, Reclamation

def index(request):
    total_chambres = Chambre.objects.count()
    total_reservations = Reservation.objects.count()
    total_clients = Client.objects.count()
    chambres_list = Chambre.objects.all()[:10]
    recent_reservations = Reservation.objects.select_related('client', 'chambre').order_by('-id')[:5]

    context = {
        'total_chambres': total_chambres,
        'total_reservations': total_reservations,
        'total_clients': total_clients,
        'chambres': chambres_list,
        'recent_reservations': recent_reservations,
    }
    return render(request, 'index.html', context)

def health_check(request):
    """Healthcheck endpoint for Kubernetes liveness/readiness probes"""
    return JsonResponse({'status': 'healthy', 'service': 'hotel-django'})
