from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView
from users.permissions import GerentePermission

from .filter import ReservaFilter
from .forms import ReservaForm
from .models import Reserva


class ReservasListView(GerentePermission, LoginRequiredMixin, FilterView):
    model = Reserva
    paginate_by = 5
    filterset_class = ReservaFilter
    template_name = "reservas/reserva_list.html"


class ReservaDetailView(GerentePermission, LoginRequiredMixin, generic.DetailView):
    model = Reserva

class ReservaCreateView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva cadastrada com sucesso!"

class ReservaUpdateView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva atualizada com sucesso!"

class ReservaDeleteView(GerentePermission, LoginRequiredMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:reservas-list")
