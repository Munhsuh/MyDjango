from django.db import models
from django.core.exceptions import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="food_images/", null=True, blank=True)
    video = models.FileField(upload_to="food_videos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Nomad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="nomad_images/", null=True, blank=True)
    video = models.FileField(upload_to="nomad_videos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="tourpackage_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")


class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




























































"""

from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

from django.conf import settings


def resize_image(image, max_size):
    
    
    if not image:
        return

    # Cloudinary images do NOT have .path
    if not hasattr(image, "path"):
        return

    try:
        img = Image.open(image.path)
        img.thumbnail(max_size)
        img.save(image.path)
    except Exception as e:
        # Never crash admin
        print("Image resize skipped:", e)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            max_size = (400, 200)  # Change as needed
            resize_image(self.image, max_size)

class Food(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    video = models.FileField(upload_to='food_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Nomad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='nomad_images/', null=True, blank=True)
    video = models.FileField(upload_to='nomad_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='tourpackage_images/', null=True, blank=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        # Add custom validation logic here
        if len(self.title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)
        if self.image:
            max_size = (400, 200)  # Change as needed
            resize_image(self.image, max_size)

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""
