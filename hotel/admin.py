from django.contrib import admin
from .models import hotel

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'longtitude', 'latitude', 'created_at', 'modified_at')
    date_hierarchy = 'created_at'
    list_filter = ('hotel_name',)
    ordering = ('id',)

admin.site.register(hotel, HotelAdmin)