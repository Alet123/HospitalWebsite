from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments, Doctors
from .foms import BookingForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def departments(request):
    obj = Departments.objects.all()
    return render(request, 'departments.html', {'result': obj})


def doctors(request):
    obj1 = Doctors.objects.all()
    return render(request, 'doctors.html', {'result1': obj1})


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)
