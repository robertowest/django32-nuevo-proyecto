# Generated by Django 3.2.7 on 2021-11-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20211112_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
