# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20160801_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferencia',
            name='codigo',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
