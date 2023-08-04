from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Booking(models.Model):
    IS_RECURRING_CHOICES = [(False, 'No'), 
                            (True, 'Yes')]
    time = models.DateTimeField()
    start_date = models.DateTimeField()    
    end_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    recurring = models.BooleanField(default=False, 
                                    choices=IS_RECURRING_CHOICES)
    member = models.ForeignKey(Member, 
                               on_delete=models.SET_NULL, 
                               related_name='booking')

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.time} - {self.member}'
    

class Guests(models.Model):
    players = models.ManyToManyField(Booking)
    date_added = models.DateTimeField(auto_now_add=True)
    member_id = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.players}'


class Subscription(models.Model):
    type = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    member = models.ForeignKey(Member, 
                               on_deletee=models.PROTECT, 
                               related_name='subscription')
    date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', 'member']

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name} - {self.date}'
    

class Messages(models.Model):
    type = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='message_sender')    
    recipients = models.ManyToManyField(Member)
    date_added = models.DateTimeField(auto_now_add=True)





