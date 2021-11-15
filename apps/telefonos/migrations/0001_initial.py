# Generated by Django 3.2.7 on 2021-11-15 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diccionarios', '0007_alter_diccionario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modified_on', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el')),
                ('texto', models.CharField(max_length=150)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
                ('tipo', models.ForeignKey(blank=True, default=1, limit_choices_to={'active': True, 'tabla': 'comunicacion'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='diccionarios.diccionario')),
            ],
            options={
                'verbose_name': 'Comunicación',
                'verbose_name_plural': 'Comunicaciones',
                'db_table': 'comunicaciones',
            },
        ),
    ]
