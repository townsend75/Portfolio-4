from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views import generic, View
from .models import UserDetails
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# make a booking and send it to the model

@login_required
def reserve(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        guests = request.POST['guests']
        date = request.POST['date']
        time = request.POST['time']
        user = User.objects.get(id=request.user.id)
        booking = UserDetails(name=name, email=email, guests=guests, date=date,
                              time=time, user=user
                              )
        booking.save()
        messages.success(request, 'Thanks! Your booking was successful!')
        

    return render(request, 'reserve.html')


def home(request):
    return render(request, 'home.html')


# view bookings made as logged in user
class Reservation(View):
   
    def get(self, request, *args, **kwargs):
        queryset = UserDetails.objects.filter(user=request.user.id)
        return render(request, 'seebooking.html',
                {"reservations": queryset},
                    )         
                   


# delete user booking

def delete(request, id):
    booking = UserDetails.objects.get(id=id)
    if not booking.user == request.user:
        messages.warning(request, 'You do not have access to this page')
        return redirect("/")
    else:
        booking.delete()
        messages.success(request, 'Your booking was deleted')
    return redirect("/reservation")


# open update form to manage booking

def update(request, id):
        booking = UserDetails.objects.get(id=id)
        if not booking.user == request.user:
            messages.warning(request, 'You do not have access to this page')
            return redirect("/")
        return render(request, "update.html", {'booking': booking})
  


# upload edited data to model
def upwrite(request, id):
    v = request.POST['name']
    w = request.POST['email']
    x = request.POST['guests']
    y = request.POST['date']
    z = request.POST['time']
    booking = UserDetails.objects.get(id=id)
    booking.name = v
    booking.email = w
    booking.guests = x
    booking.date = y
    booking.time = z
    booking.save()
    messages.success(request, 'Booking updated successfully')
    return redirect("/reservation")
