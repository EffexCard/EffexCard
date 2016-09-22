# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20160708_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='apellido',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(default='', max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
