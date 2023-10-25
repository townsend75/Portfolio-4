from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views import generic, View
from .models import Reviews, UserDetails
from django.views.generic.edit import CreateView
from .forms import BookingForm, ReviewsForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User


# class ReviewsList(generic.ListView):
#     model = Reviews
#     queryset = Reviews.objects.order_by('-created_on')
#     template_name = 'reviews.html'
#     paginate_by = 6

#     def post(self, request, *args, **kwargs):
#         queryset = UserDetails.objects.filter(customer__id=request.user.id)
#         post.save()
#         message.success(request, "Thanks, we have received your review!")
#         return render(request, 'reviews.html',
#                       {"reviews": queryset},
#                       )

# make a booking and send it to the model
def reserve(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        guests = request.POST['guests']
        date = request.POST['date']
        time = request.POST['time']
        customer = User.objects.get(id=request.user.id)
        booking = UserDetails(name=name, email=email, guests=guests, date=date, 
                              time=time, customer=customer
                              )
        booking.save()
        messages.success(request, 'Form submission successful')
     
    return render(request, 'reserve.html')
   


def home(request):
    return render(request, 'home.html')  


# view bookings made as logged in user
class Reservation(View):

    def get(self, request, *args, **kwargs):
        queryset = UserDetails.objects.filter(customer__id=request.user.id)
        
        return render(request, 'seebooking.html',
                      {"reservations": queryset},
                      )


# delete user booking   
def delete(request, id):
    booking = UserDetails.objects.get(id=id)
    booking.delete()
    messages.success(request, 'Your booking was deleted')
    return redirect("/reservation")
    

# open update form to manage booking
def update(request, id):
    booking = UserDetails.objects.get(id=id)  
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


# class ReviewsCreate(CreateView):
#     model = Reviews
#     fields = ['post', 'name', 'email', 'body', ]     


# def review(request):
#     comment = Reviews.objects.get
#     return render(request, 'reviews.html', {'comment': comment}) 


# def rev_write(request):
#     x = request.POST['name']
#     y = request.POST['email']
#     z = request.POST['body']
#     comment = Reviews.objects.get
#     comment.name = x
#     comment.email = y
#     comment.body = z
#     comment.save()
#     messages.success(request, 'Review updated successfully')
#     return redirect("/reviews")  

