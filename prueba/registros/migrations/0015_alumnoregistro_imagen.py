# Generated by Django 3.2.4 on 2021-08-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0014_remove_alumnoregistro_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnoregistro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia'),
        ),
    ]
