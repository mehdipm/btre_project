from urllib import request
from django.shortcuts import render
from listings.models import Listing
from listings.models import Realtor

def index (request):
    #get last three items of listings
    listings = \
    Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #put data in a dictionary
    context = {'listings': listings}
    #and pass it to template
    return render(request, 'pages/index.html', context)

def about (request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    #get mvp_realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    #put in dictionary for pass
    context = {"realtors": realtors,
               "mvp_realtors": mvp_realtors}

    return render(request, 'pages/about.html', context)