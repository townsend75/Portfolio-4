from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views import generic, View
from .models import Reviews, UserDetails
from django.views.generic.edit import CreateView
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User



# class ReviewsList(generic.ListView):
#     model = Reviews
#     queryset = Reviews.objects.order_by('-created_on')
#     template_name = 'home.html'
#     paginate_by = 6


# class BookingFormView(CreateView):
#     template_name = "booking.html"
#     form_class = BookingForm
#     success_url = '/home/'

# # add to your view
def get_name(request):
    
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)

    if form.is_valid():
        return render(request, 'seebooking.html')

    else:
        form = BookingForm()    

    return render(request, "get_name.html", {"form": form})
#         print("Up your arse")
#         form = BookingForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             users = UserDetails.objects.all()

#             return HttpResponseRedirect('/thanks/')


#     else:
#         form_class = BookingForm
#         args['form'] = form

#     return render(request, 'booking.html', args)   


#     def home(request):
#         return render(request, 'home.html')

def reserve(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        guests = request.POST['guests']
        date = request.POST['date']
        time = request.POST['time']
        # print(name, email, guests, date, time)
        customer = User.objects.get(id=request.user.id)
        booking = UserDetails(name=name, email=email, guests=guests, date=date, time=time, customer=customer)
        booking.save()

        messages.success(request, 'Form submission successful')
       
    return render(request, 'reserve.html')
    messages.success(request, 'Form submission successful')


def home(request):
    return render(request, 'home.html')  


class Reservation(View):

    def get(self, request, *args, **kwargs):
        queryset = UserDetails.objects.filter(customer__id=request.user.id)
        
        return render(request, 'seebooking.html',
        {"reservations": queryset},
        )

    
def delete(request, id):
    booking = UserDetails.objects.get(id=id)
    booking.delete()
    return redirect("/")
    

def update(request, id):
    booking = UserDetails.objects.get(id=id)  
    return render(request, "update.html")


def upwrite(request, id):
    w = request.POST['name']
    x = request.POST['guests']
    y = request.POST['date']
    z = request.POST['time']
    booking = UserDetails.objects.get(id=id)
    booking.name = w
    booking.guestse = x
    booking.date = y
    booking.time = z
    booking.save()
    return redirect("/")    