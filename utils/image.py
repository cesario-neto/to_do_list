from PIL import Image
from django.conf import settings
from pathlib import Path


def resize_img(image_django, new_width=400):
    img_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    img_pillow = Image.open(img_path)
    original_width, original_height = img_pillow.size

    if original_width <= 400:
        img_pillow.close()
        return img_pillow

    new_height = round((new_width * original_height) / original_width)

    new_img = img_pillow.resize((new_width, new_height))
    new_img.save(
        img_path,
        optimize=True,
    )
