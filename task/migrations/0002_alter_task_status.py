# Generated by Django 4.2.7 on 2023-12-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('finalizado', 'Finalizado')], default='pendente', max_length=100, verbose_name='Status'),
        ),
    ]
