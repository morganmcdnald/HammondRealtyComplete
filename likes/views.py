from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Like

# Create your views here.
def like(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        user_id = request.POST['user_id']

        # Check if user has liked already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_liked = Like.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_liked:
                messages.error(request, 'You have already liked this listing.')
                return redirect('/listings/'+listing_id)

        like = Like(listing=listing, listing_id=listing_id, name=name, user_id=user_id)
        like.save()

        messages.success(request, 'Your like was added successfully.')
        return redirect('/listings/'+listing_id)