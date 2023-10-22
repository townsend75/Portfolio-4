from django.shortcuts import render, get_object_or_404, HttpResponse
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
        return HttpResponseRedirect('/thanks/')

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


def home(request):
    return render(request, 'home.html')  


class Reservation(View):

    def get(self, request, *args, **kwargs):
        queryset = UserDetails.objects.filter(customer__id=request.user.id)
        
        return render(
            request,
            "seebooking.html",
            {
                "reservations": queryset
            },
        )
