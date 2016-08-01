# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_deposito_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serialcorreo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=15, verbose_name='Codigo')),
                ('valido', models.BooleanField(default=True)),
                ('email', models.CharField(default='', max_length=200, verbose_name='Email')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='usuario')),
            ],
            options={
                'db_table': 'serialcorreo',
                'verbose_name': 'Serial Correo',
                'verbose_name_plural': 'Seriales Correos',
            },
            bases=(models.Model,),
        ),
    ]
