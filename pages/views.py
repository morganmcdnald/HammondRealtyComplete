from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from blogs.models import Blog
from neighbourhoods.models import Neighbourhood
from listings.choices import price_choices, bedroom_choices, bathroom_choices
import random

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    featured_listings = Listing.objects.order_by('-price').filter(is_published=True)[:3]
    neighbourhoods = Neighbourhood.objects.order_by('name')
    blogs = Blog.objects.order_by('-post_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'featured_listings': featured_listings,
        'neighbourhoods': neighbourhoods,
        'blogs': blogs,
        'bathroom_choices': bathroom_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('hire_date')
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    # Random Listing
    all_listings = Listing.objects.all()
    random_listing = random.choice(all_listings)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'random_listing': random_listing
    }
    return render(request, 'pages/about.html', context)