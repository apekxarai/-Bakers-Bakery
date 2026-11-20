from django.contrib import admin
from .models import Sweet

@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_per_kg',
        'stock',
        'is_available'
    )
    list_filter = ('category', 'is_available')
    search_fields = ('name',)