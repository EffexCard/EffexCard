# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saldobolivianos', models.DecimalField(default=0.0, verbose_name='Saldo Bolivianos', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('saldodolares', models.DecimalField(default=0.0, verbose_name='Saldo Dolares', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('saldoeuros', models.DecimalField(default=0.0, verbose_name='Saldo Euros', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cuenta',
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuenta',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default='', max_length=45, blank=True)),
                ('apellido', models.CharField(default='', max_length=45, blank=True)),
                ('celular', models.CharField(max_length=15, blank=True)),
                ('telefono', models.CharField(max_length=15, blank=True)),
                ('foto', models.ImageField(upload_to='foto_perfil/', null=True, verbose_name='Foto', blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha de Nacimiento', db_column='fechaNacimiento', blank=True)),
                ('direccion', models.CharField(max_length=150, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'perfil',
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitudcompra',
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
                'db_table': 'solicitudcompra',
                'verbose_name': 'Solicitud de Compra',
                'verbose_name_plural': 'Solicitudes de Compra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicituddeposito',
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
                'db_table': 'solicituddeposito',
                'verbose_name': 'Solicitud de Deposito',
                'verbose_name_plural': 'Solicitudes de Deposito',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('monto', models.DecimalField(default=0.0, verbose_name='Monto', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('moneda', models.CharField(max_length=100, verbose_name='Moneda', choices=[('Bolivianos', 'Bolivianos'), ('Dolares', 'Dolares'), ('Euros', 'Euros')])),
                ('detalle', models.CharField(max_length=200, verbose_name='Detalle')),
                ('horafecha', models.DateTimeField(auto_now=True, verbose_name='Hora y Fecha')),
                ('tipo', models.CharField(default='entrada', max_length=45, blank=True, choices=[('entrada', 'entrada'), ('salida', 'salida')])),
                ('cuenta', models.ForeignKey(to='webapp.Cuenta', db_column='cuenta')),
                ('responsable', models.ForeignKey(default=None, verbose_name='Responsable', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transferencia',
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
            bases=(models.Model,),
        ),
    ]
