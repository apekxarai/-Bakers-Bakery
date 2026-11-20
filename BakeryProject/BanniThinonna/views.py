
from django.shortcuts import render
from .models import Sweet


def home(request):
    return render(request, 'home.html')


def sweets(request):
    all_sweets = Sweet.objects.filter(
        is_available=True
    ).order_by('name')

    return render(request, 'sweets.html', {
        'sweets': all_sweets
    })


def cart(request):
    return render(request, 'cart.html', {
        'cart_items': [],
        'total': 0
    })


def wishlist(request):
    return render(request, 'wishlist.html', {
        'wishlist_items': []
    })
