# Generated by Django 3.2.7 on 2021-10-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diccionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diccionario',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='diccionario',
            name='date_deleted',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Eliminación'),
        ),
        migrations.AlterField(
            model_name='diccionario',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Modificación'),
        ),
    ]