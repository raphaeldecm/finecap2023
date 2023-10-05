from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


# Create your views here.
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"
