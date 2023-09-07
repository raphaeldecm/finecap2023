from django.shortcuts import get_object_or_404, render

from .models import Reserva


# Create your views here.
def index(request):
    return render(request, "index.html")

def reservas_list(request):
    context = {
        "reservas": Reserva.objects.all()
    }
    return render(request, "reservas_list.html", context)

def reservas_detail(request, id):
    obj = get_object_or_404(Reserva, id=id)
    return render(request, "reservas_detail.html", {"object": obj})
