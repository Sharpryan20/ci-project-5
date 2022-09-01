from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('contact', views.contact, name='contact'),
]
