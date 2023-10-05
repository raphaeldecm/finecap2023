from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import ReservaForm
from .models import Reserva


class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    paginate_by = 5

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva

class ReservaCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva cadastrada com sucesso!"

class ReservaUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva atualizada com sucesso!"

class ReservaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:reservas-list")
