from django.contrib import messages
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import ReservaForm
from .models import Reserva


class ReservasListView(generic.ListView):
    model = Reserva
    paginate_by = 5

class ReservaDetailView(generic.DetailView):
    model = Reserva

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva cadastrada com sucesso!"
    error_message = "Erro ao cadastrar reserva!"

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva atualizada com sucesso!"

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:reservas-list")
