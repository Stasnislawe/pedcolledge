from django.contrib import admin
from .models import Users, TestResults, UserAnswers, Quizzes, Questions, Options


admin.site.register(Users)
admin.site.register(TestResults)
admin.site.register(UserAnswers)
admin.site.register(Quizzes)
admin.site.register(Questions)
admin.site.register(Options)