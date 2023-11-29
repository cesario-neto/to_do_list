from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name='Identificador',
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    created_at = models.DateTimeField(
        verbose_name='Criado às', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Atualizado às', auto_now=True)

    class Meta:
        abstract = True
