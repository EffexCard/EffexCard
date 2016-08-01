# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20160708_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='moneda',
        ),
        migrations.AlterField(
            model_name='compra',
            name='preciototal',
            field=models.DecimalField(default=0.0, verbose_name='Precio Total (Bs.)', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deposito',
            name='monto',
            field=models.DecimalField(default=0.0, verbose_name='Monto (Bs.)', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
    ]
