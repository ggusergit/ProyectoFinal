# Generated by Django 4.2.2 on 2023-08-18 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPublicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
