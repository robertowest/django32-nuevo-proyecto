# Generated by Django 3.2.7 on 2021-10-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diccionarios', '0003_auto_20211014_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diccionario',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='diccionario',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el'),
        ),
    ]