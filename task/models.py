from django.db import models
from core.models import BaseModel
from django.utils.text import slugify
from account.models import User


class Task(BaseModel):
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    f = 'finalizado'
    p = 'pendente'
    choices = (
        (p, 'Pendente'),
        (f, 'Finalizado'),
    )

    user = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    title = models.CharField(verbose_name='Título',
                             max_length=100, blank=True, null=True)
    task_text = models.TextField(
        verbose_name='Tarefa', blank=False, null=False)
    end_in = models.DateTimeField(verbose_name='Terminar em')
    status = models.CharField(
        verbose_name='Status',
        choices=choices, max_length=100,
        blank=False,
        null=False, default=p
    )
    slug = models.SlugField(verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
