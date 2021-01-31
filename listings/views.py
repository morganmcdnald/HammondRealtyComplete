from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, bathroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Neighbourhood
    if 'neighbourhood' in request.GET:
        neighbourhood = request.GET['neighbourhood']
        if neighbourhood:
            queryset_list = queryset_list.filter(neighbourhood__name__iexact=neighbourhood)

    # Max Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Min Bedrooms
    if 'minbedrooms' in request.GET:
        minbedrooms = request.GET['minbedrooms']
        if minbedrooms:
            queryset_list = queryset_list.filter(bedrooms__gte=minbedrooms)

    # Max Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Min Price
    if 'minprice' in request.GET:
        minprice = request.GET['minprice']
        if minprice:
            queryset_list = queryset_list.filter(price__gte=minprice)

    # Max Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)

    # Min Bathrooms
    if 'minbathrooms' in request.GET:
        minbathrooms = request.GET['minbathrooms']
        if minbathrooms:
            queryset_list = queryset_list.filter(bathrooms__gte=minbathrooms)

    context = {
        'bathroom_choices': bathroom_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)