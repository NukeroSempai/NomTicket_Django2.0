# Generated by Django 3.1.2 on 2021-05-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0006_auto_20210523_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='clave',
            field=models.CharField(default='a', max_length=50, verbose_name='contraseña'),
            preserve_default=False,
        ),
    ]
