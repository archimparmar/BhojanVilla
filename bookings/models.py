from django.db import models
from django.contrib.auth.models import User

from django.db import models
from website.models import WebsiteImage  # Ensure correct import

class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard Room'),
        ('deluxe', 'Deluxe Room'),
        ('family', 'Family Room'),
        ('suite', 'Luxury Suite'),
        ('garden', 'Garden View Room'),
        ('poolside', 'Poolside Room'),
        ('executive', 'Executive Room'),
        ('honeymoon', 'Honeymoon Suite'),
        ('heritage', 'Heritage Room'),
        ('tent', 'Tent Cottage'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    num_beds = models.PositiveIntegerField(default=1) 
    max_occupancy = models.PositiveIntegerField(default=2)
    is_available = models.BooleanField(default=True)
    image = models.ForeignKey(
        WebsiteImage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'category': 'room_image'},  
        related_name='room_images'
    )

    def __str__(self):
        return self.title

class RoomBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    special_requests = models.TextField(blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending' 
    )

    def __str__(self):
        return f"{self.user.username} - {self.room.title} Booking"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.OneToOneField(
        'Table', on_delete=models.CASCADE, null=True, blank=True)
    booking_datetime = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.booking_datetime}"


class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
