# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20160720_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='email',
            field=models.CharField(default='', max_length=200, verbose_name='Email'),
            preserve_default=True,
        ),
    ]
