from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrationView.as_view(), name='register'),
    path('registered/', views.SuccessfullyRegisteredView.as_view(), name='successfully_registered')
]