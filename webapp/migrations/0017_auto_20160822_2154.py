# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_transferencia_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposito',
            name='adjunto',
            field=models.FileField(help_text='a\xf1adir solo archivos PDF o Imagenes', upload_to='archivo_solicituddeposito/', null=True, verbose_name='Adjuntar Comprobante', blank=True),
            preserve_default=True,
        ),
    ]
