# Generated by Django 5.0 on 2023-12-10 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_categoria_alter_publicacion_creador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publicaciones', to='publicaciones.categoria'),
        ),
    ]
