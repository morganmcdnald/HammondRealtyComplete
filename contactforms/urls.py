from django.urls import path
from . import views

urlpatterns = [
    path('contactform', views.contactform, name='contactform')
]