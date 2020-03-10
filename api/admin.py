from django.contrib import admin
from .models import Hotel, HotelImage


# Register your models here.

class HotelImageInline(admin.TabularInline):
    model = HotelImage


class HotelAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    inlines = [
        HotelImageInline,
    ]

admin.site.register(Hotel, HotelAdmin)
