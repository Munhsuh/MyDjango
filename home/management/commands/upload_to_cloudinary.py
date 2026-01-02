from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
import os

from home.models import TourPackage, Food, Nomad, Post


class Command(BaseCommand):
    help = "Upload existing local images to Cloudinary"

    def handle(self, *args, **kwargs):
        models_with_images = [TourPackage, Food, Nomad, Post]

        for model in models_with_images:
            self.stdout.write(f"\nProcessing model: {model.__name__}")

            for obj in model.objects.all():
                image_field = getattr(obj, "image", None)

                if not image_field or not image_field.name:
                    self.stdout.write(f"No image for {model.__name__} id={obj.id}")
                    continue

                local_path = os.path.join(settings.MEDIA_ROOT, image_field.name)

                if not os.path.exists(local_path):
                    self.stdout.write(f"File NOT found: {local_path}")
                    continue

                with open(local_path, "rb") as f:
                    image_field.save(
                        os.path.basename(image_field.name),
                        File(f),
                        save=True,
                    )

                self.stdout.write(f"Uploaded → {model.__name__} id={obj.id}")
