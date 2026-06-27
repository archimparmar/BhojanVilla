from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, Table
from website.forms import BookingForm
from .models import Room
from .forms import RoomBookingForm
from bookings.models import RoomBooking


def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'bookings/room_list.html', {'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = RoomBookingForm()
    return render(request, 'bookings/book_room.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('profile')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/update_table_booking_form.html', {'form': form})


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('profile')


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def update_room_booking(request, booking_id):
    booking = get_object_or_404(RoomBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RoomBookingForm(instance=booking)
    return render(request, 'bookings/room_booking_form.html', {'form': form})

@login_required
def cancel_room_booking(request, booking_id):
    booking = get_object_or_404(RoomBooking, pk=booking_id, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('profile')
