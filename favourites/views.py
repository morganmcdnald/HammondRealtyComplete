from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Favourite

# Create your views here.
def favourite(request):
    if request.method == 'POST':
        blog_id = request.POST['blog_id']
        blog = request.POST['blog']
        username = request.POST['username']
        user_id = request.POST['user_id']

        favourite = Favourite(blog=blog, blog_id=blog_id, username=username, user_id=user_id)
        favourite.save()

        messages.success(request, 'Your like was added successfully.')
        return redirect('/blogs/'+blog_id)