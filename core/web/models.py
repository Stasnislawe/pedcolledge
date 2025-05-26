from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(unique=True)
    family_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    patronymic = models.TextField()
    birth_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    email = models.EmailField()
    phone_number = models.TextField()
    username = models.CharField(max_length=250)
    registration_time = models.DateField()
    created_at = models.DateField()
    password = models.TextField()


class UserAnswers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='useranswer_id')
    question_text = models.TextField()
    answer_text = models.TextField()
    points = models.IntegerField()
    binary_answer = models.BooleanField()
    test_session_id = models.BigIntegerField()
    answer_time = models.TimeField()
    created_at = models.DateField()


class TestResults(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='testresults_id')
    test_session_id = models.BigIntegerField()
    total_points = models.IntegerField()
    binary_score = models.IntegerField()
    gender_score = models.IntegerField()
    probability = models.FloatField()
    prob_range = models.FloatField()
    created_at = models.DateField()


class Quizzes(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateField()


class Questions(models.Model):
    quiz_id = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_order = models.IntegerField()
    created_ad = models.DateField()


class Options(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_text = models.TextField()
    points = models.IntegerField()
    binary_value = models.BooleanField()
    created_at = models.DateField()