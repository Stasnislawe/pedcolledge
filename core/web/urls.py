from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IndexView, CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('index/', IndexView.as_view(), name='index'),
]
