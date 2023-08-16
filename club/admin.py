from django.contrib import admin

from .models import Member, Booking, Subscription, Messages

admin.site.register(Member)
admin.site.register(Booking)
admin.site.register(Subscription)
admin.site.register(Messages)