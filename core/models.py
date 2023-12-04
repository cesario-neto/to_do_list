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


class SiteSetup(BaseModel):
    class Meta:
        verbose_name = 'Configuração do site'
        verbose_name_plural = 'Configurações do site'

    header = models.BooleanField(verbose_name='Cabeçalho', default=True)
    header_title = models.CharField(
        verbose_name='Titulo do cabeçalho', max_length=60)
    footer = models.BooleanField(verbose_name='Rodapé', default=True)
    footer_text = models.CharField(
        verbose_name='Texto do rodapé', max_length=60)
