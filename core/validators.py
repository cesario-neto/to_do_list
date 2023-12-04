from django.core.exceptions import ValidationError


def validate_img(img):
    if not img.name.endswith('.png'):
        raise ValidationError(
            'Imagem inválida, somente imagens png'
        )
