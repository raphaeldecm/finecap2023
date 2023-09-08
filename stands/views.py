from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservaForm
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

def reservas_create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect("stands:reservas-list")
    else:
        form = ReservaForm()
    
    return render(request, "reservas_form.html", {"form": form})

def reservas_update(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return redirect("stands:reservas-list")
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas_form.html', {"form": form})

def reservas_delete(request, id):
    get_object_or_404(Reserva, id=id).delete()
    return redirect("stands:reservas-list")
