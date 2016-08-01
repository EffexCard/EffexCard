# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_remove_transferencia_moneda'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposito',
            name='codigo',
            field=models.CharField(default='', max_length=100, verbose_name='Numero de Transacci\xf3n'),
            preserve_default=False,
        ),
    ]
