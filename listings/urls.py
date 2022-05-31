from unicodedata import name

from django.conf import settings
from . import views
from django.urls import path

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]