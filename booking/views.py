from django.shortcuts import render
from django.views import generic
from .models import Reviews
from django.views.generic.edit import FormView
from .forms import BookingForm


class ReviewsList(generic.ListView):
    model = Reviews
    queryset = Reviews.objects.order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6


class BookingFormView(FormView):
    template_name = "booking.html"
    form_class = BookingForm
