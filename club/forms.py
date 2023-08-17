from .models import Booking

from django import forms
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date','recurring', 'owner','players']

    def clean_players(self):
        players = self.cleaned_data.get('authors')
        if players and players > 4:
            raise ValidationError("Only 4 players per booking")
        return players
   