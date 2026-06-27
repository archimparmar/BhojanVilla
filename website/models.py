from django.db import models
# import cloudinary
# import cloudinary.uploader
# import cloudinary.models
from django_summernote.fields import SummernoteTextField

# Create your models here.


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_details = models.TextField()
    opening_hours = models.TextField()
    description = models.TextField(blank=True)
    about_us = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class WebsiteImage(models.Model):
    IMAGE_CATEGORIES = [
        ('hero', 'Hero Image'),
        ('background', 'Background Image'),
        ('menu', 'Menu Item Image'),
        ('gallery', 'Gallery Image'),
        ('room_image', 'Room Image'),
        ('featured_dish', 'Featured Dish Image'),
        ('testimonial_background', 'Testimonial Background Image'),
        ('history_background', 'History Background Image'),
        ('team_member', 'Team Member Image'),
    ]

    name = models.CharField(max_length=100, blank= True)
    category = models.CharField(max_length=25, choices=IMAGE_CATEGORIES)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class MenuPost(models.Model):
    title = models.CharField(max_length=200)
    content = SummernoteTextField(blank=True)
    image = models.ForeignKey('WebsiteImage', on_delete=models.SET_NULL,
                              null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Dish(models.Model):
    menu_post = models.ForeignKey(MenuPost, related_name='dishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
