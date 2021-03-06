# Generated by Django 3.1.2 on 2021-05-20 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0004_auto_20210520_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='saldo',
            field=models.PositiveIntegerField(null=True, verbose_name='cargar saldo'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fk_tipo_ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='CORE.tipo_ticket'),
            preserve_default=False,
        ),
    ]
