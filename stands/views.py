from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ReservaForm
from .models import Reserva


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "index.html"

class ReservasListView(generic.ListView):
    model = Reserva

class ReservaDetailView(generic.DetailView):
    model = Reserva

class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("stands:reservas-list")

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("stands:reservas-list")

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("stands:reservas-list")
