# Generated by Django 5.0.4 on 2024-04-26 20:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]