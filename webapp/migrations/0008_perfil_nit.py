# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_compra_tienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nit',
            field=models.CharField(default='', max_length=20, verbose_name='Carnet o NIT', blank=True),
            preserve_default=True,
        ),
    ]
