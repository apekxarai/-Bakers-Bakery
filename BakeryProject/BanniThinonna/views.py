
from django.shortcuts import render, get_object_or_404
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


def sweet_detail(request, sweet_id):
    sweet = get_object_or_404(
        Sweet,
        id=sweet_id,
        is_available=True
    )

    similar_sweets = Sweet.objects.filter(
        category=sweet.category,
        is_available=True
    ).exclude(id=sweet.id)[:4]

    return render(request, 'sweet_detail.html', {
        'sweet': sweet,
        'similar_sweets': similar_sweets
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
