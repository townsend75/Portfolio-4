from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic, View
from .models import Reviews, Person
from django.views.generic.edit import CreateView
from .forms import BookingForm
from django.http import HttpResponseRedirect



# class ReviewsList(generic.ListView):
#     model = Reviews
#     queryset = Reviews.objects.order_by('-created_on')
#     template_name = 'home.html'
#     paginate_by = 6


# class BookingFormView(CreateView):
#     template_name = "booking.html"
#     form_class = BookingForm
#     success_url = '/home/'


# # add to your views
# def Booking(request):
#     form = BookingForm()
#     args = {}
#     if request.method == 'POST':
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
        ins = Person(name=name, email=email, guests=guests, date=date, time=time)
        ins.save()
        print("The data is now on the database")

    return render(request, 'reserve.html')


def home(request):
    return render(request, 'home.html')  


class reservation(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Person.objects.filter(status=1)
        reservation = get_object_or_404(queryset, slug=slug)
        

        return render(
            request,
            "seebooking.html",
            {
                "name": name,
                "email": email,
                "guests": guests,
                "date": date,
                "time": time
            },
        )
