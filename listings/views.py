from django.shortcuts import render
from .models import Listing
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

def index (request):
    #pull data from database and order by date . publish or not
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    #dictionary that will pass to template
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)

def listing (request, listing_id):
    return render(request, 'listings/listing.html')

def search (request):
    return render(request, 'listings/search.html')
