from django.contrib import admin
from .models import Person, Reviews
from django_summernote.admin import SummernoteModelAdmin
from .forms import BookingForm


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):

    search_fields = ('name', 'email', 'body')
    summernote_fields = ("body")


@admin.register(Person)
class BookingAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'guests', 'date', 'time')
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(approved=True)
    