from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from .filters import StandFilter
from .forms import StandForm
from .models import Stand


# Create your views here.
class StandsListView(LoginRequiredMixin, FilterView):
    model = Stand
    paginate_by = 5
    ordering = ["-created_at"]
    filterset_class = StandFilter
    template_name = "stands/stand_list.html"

    def get_queryset(self):
        return Stand.objects.filter(created_by=self.request.user)

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand

class StandCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class StandUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand atualizada com sucesso!"

class StandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stands:stands-list")
    success_message = "Stand excluído com sucesso!"
