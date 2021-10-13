# Generated by Django 3.2.7 on 2021-10-05 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AddField(
            model_name='book',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado'),
        ),
        migrations.AddField(
            model_name='book',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
        migrations.AddField(
            model_name='book',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]