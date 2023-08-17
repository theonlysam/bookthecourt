from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.Booking, name='add_booking' ),
    
]