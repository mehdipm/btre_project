from django.shortcuts import get_object_or_404, render
from .models import Listing, Realtor
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
    #get listings item by id
    listing = get_object_or_404(Listing, pk=listing_id)
    realtors = Realtor.objects.all().filter(is_mvp=True)
    #put in dictionary for pass
    context = {'listing': listing, 'realtors': realtors}
    return render(request, 'listings/listing.html', context)

def search (request):
    return render(request, 'listings/search.html')
