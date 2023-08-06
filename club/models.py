from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    TYPE_CHOICES = [('Admin', 'Admin'),
                    ('Local', 'Local'),
                    ('Foreign', 'Foreign')]
    
    email = models.EmailField(unique=True)
    type = models.CharField(choices=TYPE_CHOICES)
    address = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Booking(models.Model):      
    start_date = models.DateTimeField()    
    end_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    recurring = models.BooleanField(default=False)
    owner = models.ForeignKey(Member, 
                               on_delete=models.SET_NULL, 
                               related_name='booking')
    players = models.ManyToManyField(Member)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.time} - {self.member}'
    

# class Guests(models.Model):
#     players = models.ManyToManyField(Booking)
#     date_added = models.DateTimeField(auto_now_add=True)
#     member_id = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.players}'


class Subscription(models.Model):
    type = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    member = models.ForeignKey(Member, 
                               on_deletee=models.PROTECT, 
                               related_name='subscription')
    date = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_added', 'member']

    def __str__(self):
        return f'{self.member} - {self.date}'
    

class Messages(models.Model):
    TYPE_CHOICES = [('Booking Change', 'Booking Change'),
                    ('New Booking', 'New Booking'),
                    ('Admin', 'Admin'),
                    ('Member', 'Member')]
    
    type = models.CharField(choices=TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='message_sender')    
    recipients = models.ManyToManyField(Member)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.sender} - {self.subject}'





