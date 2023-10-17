from django.contrib import admin
from .models import Booking, Reviews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):

    search_fields = ('name', 'email', 'body')
    summernote_fields = ("body")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number_of_guests', 'date', 'time')
    search_fields = ['title', 'content']
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(approved=True)
    