# Generated by Django 4.2.5 on 2023-10-13 13:09

from django.db import migrations, models
import stands.validators


class Migration(migrations.Migration):

    dependencies = [
        ('stands', '0002_delete_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='localizacao',
            field=models.CharField(max_length=50, validators=[stands.validators.validate_stand_localizacao], verbose_name='Localização'),
        ),
    ]
