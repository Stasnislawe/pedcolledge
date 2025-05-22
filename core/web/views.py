from django.shortcuts import render
from django.views.generic import ListView
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'index.html'

