from django.shortcuts import render
from django.views.generic import ListView
from .models import UserAnswers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django_ratelimit.decorators import ratelimit


class IndexView(LoginRequiredMixin, ListView):
    model = UserAnswers
    context_object_name = 'patients'
    template_name = 'index.html'


class CustomLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', method='POST')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)