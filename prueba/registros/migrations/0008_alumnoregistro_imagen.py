# Generated by Django 3.2.4 on 2021-08-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_alumnoregistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnoregistro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]