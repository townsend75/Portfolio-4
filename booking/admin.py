from django.contrib import admin
from .models import UserDetails
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserDetails)
class BookingAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'guests', 'date', 'time')
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(approved=True)
