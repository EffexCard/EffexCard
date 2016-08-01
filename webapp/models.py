# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
from django.conf import settings

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nit = models.CharField(max_length=20, blank=True,default="",verbose_name="Carnet o NIT",help_text='Use el siguiente formato XXXXXXXLP')
    nombre = models.CharField(max_length=250, blank=True,default="")
    celular = models.CharField(max_length=15, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    foto = models.ImageField(upload_to="foto_perfil/",blank=True,null=True,verbose_name = "Foto",help_text="En lo posible, utilice imagénes cuadradas.")
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento', blank=True,verbose_name='Fecha de Nacimiento',null=True)
    direccion = models.CharField(max_length=150, blank=True)

    class Meta: 
        #managed = False
        db_table = 'perfil'
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __unicode__(self):
        return unicode(self.user)

class Cuenta(models.Model):
    moneda_opciones = (
        ('Bolivianos', 'Bolivianos'),
        ('Dolares', 'Dolares'),
        ('Euros', 'Euros'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    saldo = models.DecimalField(default=0.0,max_digits=10, decimal_places=2,verbose_name='Saldo',validators=[MinValueValidator(0.0)])
    moneda = models.CharField(max_length=100,verbose_name='Moneda',choices=moneda_opciones,default="Bolivianos")
    class Meta: 
        db_table = "cuenta"
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuenta"

    def __unicode__(self):
        return unicode(self.user)

class Deposito(models.Model):
    estado_opciones = (
        ('Aceptado', 'Aceptado'),
        ('Pendiente', 'Pendiente'),
        ('Rechazado', 'Rechazado'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='usuario')
    monto = models.DecimalField(default=0.0,max_digits=10, decimal_places=2,verbose_name='Monto (Bs.)',validators=[MinValueValidator(0.0)])
    fecha = models.DateField(auto_now=True,verbose_name='Fecha')
    adjunto = models.FileField(upload_to='archivo_solicituddeposito/',verbose_name = "Adjuntar Comprobante",null=True,blank=True,help_text="añadir solo archivos PDF o Imagenes",)
    codigo = models.CharField(max_length=100,verbose_name='Numero de Transacción',)
    estado = models.CharField(max_length=100,verbose_name='Estado',choices=estado_opciones)
    class Meta:
        #managed = False
        db_table = 'deposito'
        verbose_name = "Deposito"
        verbose_name_plural = "Deposito"

    def __unicode__(self):
        return str(self.id)

class Compra(models.Model):
    
    estado_opciones = (
        ('Aceptado', 'Aceptado'),
        ('Pendiente', 'Pendiente'),
        ('Rechazado', 'Rechazado'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='usuario')
    producto = models.CharField(max_length=300)
    preciototal = models.DecimalField(default=0.0,max_digits=10, decimal_places=2,verbose_name='Precio Total (Bs.)',validators=[MinValueValidator(0.0)])
    cantidad = models.IntegerField(default=1)
    descripcion = models.TextField(max_length=5000,verbose_name='Descripción (talla, color, marca, referencia, etc.)')
    fecha = models.DateField(auto_now=True,verbose_name='Fecha')
    tienda = models.CharField(max_length=300,verbose_name="Tienda")
    direccionurl = models.CharField(max_length=1000,verbose_name="Dirección URL/Enlace del Producto")
    estado = models.CharField(max_length=100,verbose_name='Estado',choices=estado_opciones)
    class Meta:
        #managed = False
        db_table = 'compra'
        verbose_name = "Compra"
        verbose_name_plural = "Compra"

    def __unicode__(self):
        return str(self.id)

class Transferencia(models.Model):
    opciones = (
        ('entrada', 'entrada'),
        ('salida', 'salida'),)

    id = models.AutoField(primary_key=True)
    monto = models.DecimalField(default=0.0,max_digits=10, decimal_places=2,verbose_name='Monto',validators=[MinValueValidator(0.0)])
    detalle = models.CharField(max_length=200,verbose_name='Detalle')
    horafecha = models.DateTimeField(auto_now=True,verbose_name='Hora y Fecha')
    tipo = models.CharField(max_length=45, blank=True,choices=opciones,default="entrada")
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL,default=None,verbose_name = "Responsable")
    cuenta = models.ForeignKey(Cuenta, db_column='cuenta')
    class Meta:
        #managed = False
        db_table = 'transferencia'
        verbose_name = "Transferencia"
        verbose_name_plural = "Transferencias"

    def __unicode__(self):
        return str(self.id)

class Serial(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=15,verbose_name='Codigo')
    valido = models.BooleanField(default=True)
    email = models.CharField(default="",max_length=200, verbose_name="Email",)
    class Meta:
        #managed = False
        db_table = 'serial'
        verbose_name = "Serial"
        verbose_name_plural = "Seriales"

    def __unicode__(self):
        return str(self.id)

class Serialcorreo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='usuario')
    codigo = models.CharField(max_length=15,verbose_name='Codigo')
    valido = models.BooleanField(default=True)
    email = models.CharField(default="",max_length=200, verbose_name="Email",)
    class Meta:
        #managed = False
        db_table = 'serialcorreo'
        verbose_name = "Serial Correo"
        verbose_name_plural = "Seriales Correos"

    def __unicode__(self):
        return str(self.id)