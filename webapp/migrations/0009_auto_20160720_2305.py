# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_perfil_nit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=15, verbose_name='Codigo')),
                ('valido', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'serial',
                'verbose_name': 'Serial',
                'verbose_name_plural': 'Seriales',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(help_text='En lo posible, utilice imag\xe9nes cuadradas.', upload_to='foto_perfil/', null=True, verbose_name='Foto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nit',
            field=models.CharField(default='', help_text='Use el siguiente formato XXXXXXXLP', max_length=20, verbose_name='Carnet o NIT', blank=True),
            preserve_default=True,
        ),
    ]
