from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contactform

# Create your views here.
def contactform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']

    contactform = Contactform(name=name, email=email, subject=subject, message=message, user_id=user_id)
    contactform.save()

    messages.success(request, 'Your message was successfully submitted, a realtor will get back to you ASAP.')
    return redirect('/')