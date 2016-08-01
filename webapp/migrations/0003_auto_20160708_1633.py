# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20160626_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='saldobolivianos',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='saldodolares',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='saldoeuros',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='moneda',
            field=models.CharField(default='Bolivianos', max_length=100, verbose_name='Moneda', choices=[('Bolivianos', 'Bolivianos'), ('Dolares', 'Dolares'), ('Euros', 'Euros')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='saldo',
            field=models.DecimalField(default=0.0, verbose_name='Saldo', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
    ]
