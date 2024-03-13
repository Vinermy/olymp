from django.urls import path

from olymp_app import views

urlpatterns = [
    path('auth/login', views.login, name='login'),
]