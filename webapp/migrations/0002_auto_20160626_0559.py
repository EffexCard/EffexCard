# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('producto', models.CharField(max_length=300)),
                ('preciototal', models.DecimalField(default=0.0, verbose_name='Precio Total', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('moneda', models.CharField(max_length=100, verbose_name='Moneda', choices=[('Bolivianos', 'Bolivianos'), ('Dolares', 'Dolares'), ('Euros', 'Euros')])),
                ('cantidad', models.IntegerField(default=1)),
                ('descripcion', models.TextField(max_length=5000, verbose_name='Descripci\xf3n (talla, color, marca, referencia, etc.)')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('direccionurl', models.CharField(max_length=1000, verbose_name='Direcci\xf3n URL/Enlace del Producto')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado', choices=[('Aceptado', 'Aceptado'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado'), ('Cancelado', 'Cancelado')])),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='usuario')),
            ],
            options={
                'db_table': 'compra',
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('monto', models.DecimalField(default=0.0, verbose_name='Monto', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('moneda', models.CharField(max_length=100, verbose_name='Moneda', choices=[('Bolivianos', 'Bolivianos'), ('Dolares', 'Dolares'), ('Euros', 'Euros')])),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('adjunto', models.FileField(help_text='a\xf1adir solo archivos PDF o Imagenes', upload_to='archivo_solicituddeposito/', null=True, verbose_name='Adjuntar Comprobante', blank=True)),
                ('estado', models.CharField(max_length=100, verbose_name='Estado', choices=[('Aceptado', 'Aceptado'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado'), ('Cancelado', 'Cancelado')])),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column='usuario')),
            ],
            options={
                'db_table': 'deposito',
                'verbose_name': 'Deposito',
                'verbose_name_plural': 'Deposito',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='solicitudcompra',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Solicitudcompra',
        ),
        migrations.RemoveField(
            model_name='solicituddeposito',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Solicituddeposito',
        ),
    ]
