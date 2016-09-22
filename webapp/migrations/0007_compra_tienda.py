# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20160708_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='tienda',
            field=models.CharField(default='', max_length=300, verbose_name='Tienda'),
            preserve_default=False,
        ),
    ]
