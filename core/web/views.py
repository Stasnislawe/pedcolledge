from django.shortcuts import render
from django.views.generic import ListView
from .models import UserAnswers
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    model = UserAnswers
    context_object_name = 'patients'
    template_name = 'index.html'

