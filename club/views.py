from django.shortcuts import render
from django.views import View


class CreateBookingView(View):

    def get(self, request, *args, **kwargs):
        pass
        # select all bookings for today and tomorrow

    def post(self, request, *args, **kwargs):
        pass


