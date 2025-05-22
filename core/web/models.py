from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm


class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    last_questionnaire = models.CharField(max_length=50)
    rating = models.CharField(max_length=7, default='neutral')


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",
                  "password1",
                  "password2", )