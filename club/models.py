from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class Member(AbstractUser):
    TYPE_CHOICES = [('Admin', 'Admin'),
                    ('Local', 'Local'),
                    ('Foreign', 'Foreign')]
    
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    address = models.CharField(max_length=100)
    home_phone = PhoneField(blank=True, help_text='Home phone number')
    mobile = PhoneField(blank=True, help_text='Mobile number')
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.username}'
    
    
class Booking(models.Model):      
    start_date = models.DateTimeField()    
    end_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    recurring = models.BooleanField(default=False, blank=True, null=True)
    owner = models.ForeignKey(Member, 
                               on_delete=models.PROTECT, 
                               related_name='booked_by')
    players = models.ManyToManyField(Member, related_name='players')

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.start_date} - {self.member}'
    

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
                               on_delete=models.PROTECT, 
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
    
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='message_sender')    
    recipients = models.ManyToManyField(Member)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.sender} - {self.subject}'





