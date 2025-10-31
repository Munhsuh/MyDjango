from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError

def resize_image(image, max_size):
    """Resizes an image to the given maximum size."""
    img_path = image.path
    img = Image.open(img_path)
    img.thumbnail(max_size)
    img.save(img_path)

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



