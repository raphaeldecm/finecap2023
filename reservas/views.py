from django.contrib.messages import views
from django.forms.models import BaseModelForm
from django.http import HttpResponse
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

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print("## ", form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas-list")
    success_message = "Reserva atualizada com sucesso!"

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:reservas-list")
