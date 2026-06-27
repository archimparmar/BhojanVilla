from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('update/<int:pk>/', views.update_booking, name='update_booking'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('list/', views.booking_list, name='booking_list'),
]

urlpatterns += [
    path('rooms/', views.room_list, name='room_list'),
    path('book-room/', views.book_room, name='book_room'),
    path('booking-success/', views.booking_success, name='booking_success'), 
    path('room-booking/<int:booking_id>/edit/', views.update_room_booking, name='update_room_booking'),
    path('room-booking/<int:booking_id>/cancel/', views.cancel_room_booking, name='cancel_room_booking'),
]