# Generated by Django 3.1.4 on 2021-05-24 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0002_auto_20210520_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='clave',
            field=models.CharField(max_length=50, verbose_name='contraseña'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.perfil', verbose_name='Perfil'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.turno', verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='saldo',
            field=models.PositiveIntegerField(choices=[(264000, 'Administración 264000'), (378000, 'Jefaturas 378000'), (450000, 'Gerente 450000'), (276000, 'Operarios 276000')], default=0, verbose_name='cargar saldo'),
        ),
    ]