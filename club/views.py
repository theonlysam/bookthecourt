from django.shortcuts import render
from django.contrib import messages

from .forms import BookingForm



def Booking(request):

    if request.method == "GET":
        form = BookingForm()

    elif request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking added successfully')
            form = BookingForm()

    context = {
        "form": form,
    }
    return render(request, 'club/booking.html', context)

