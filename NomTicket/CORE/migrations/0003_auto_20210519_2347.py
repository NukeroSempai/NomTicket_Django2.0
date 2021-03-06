# Generated by Django 3.1.2 on 2021-05-20 03:47

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0002_auto_20210519_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='clave',
            field=fernet_fields.fields.EncryptedCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_empresa',
            field=models.ForeignKey(help_text='Empresa', on_delete=django.db.models.deletion.PROTECT, to='CORE.empresa'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_perfil',
            field=models.ForeignKey(help_text='Prefil', on_delete=django.db.models.deletion.PROTECT, to='CORE.perfil'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_turno',
            field=models.ForeignKey(help_text='Turno', on_delete=django.db.models.deletion.PROTECT, to='CORE.turno'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='saldo',
            field=models.PositiveIntegerField(choices=[(264000, 'Administración 264000'), (378000, 'Jefaturas 378000'), (450000, 'Gerente 450000'), (276000, 'Operarios 276000')], default=276000, verbose_name='Cargar Saldo'),
        ),
    ]
