# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404,redirect
from webapp.models import *
from django.template import RequestContext,loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from webapp.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from datetime import datetime, timedelta,date,time
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.utils import formats
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
import random, string
from django.contrib.sites.models import Site
from decimal import Decimal

#WEBSITE
def store(request):
    ctx = {}
    return render_to_response('store.html',ctx,context_instance=RequestContext(request))

def website(request):
    ctx = {}
    return render_to_response('website/website.html',ctx,context_instance=RequestContext(request))

def quienes_somos(request):
    ctx = {}
    return render_to_response('website/quienes_somos.html',ctx,context_instance=RequestContext(request))

def quiero_negocio(request):
    ctx = {}
    return render_to_response('website/quiero_negocio.html',ctx,context_instance=RequestContext(request))

def ayuda(request):
    ctx = {}
    return render_to_response('website/ayuda.html',ctx,context_instance=RequestContext(request))


#WEBAPP
def control_ingreso(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home') 
    else:
        return HttpResponseRedirect('/login')

@login_required()
def home(request):
    cuenta = Cuenta.objects.filter(user=request.user)[0]  
    compras = Compra.objects.filter(usuario=request.user).order_by('-id')
    depositos = Deposito.objects.filter(usuario=request.user).order_by('-id')
    movimientos = Transferencia.objects.filter(cuenta__user=request.user).order_by('-id')

    ctx = {'cuenta':cuenta,'compras':compras,'depositos':depositos,'movimientos':movimientos}
    return render_to_response('webapp/home.html', ctx, context_instance=RequestContext(request))

#VISTA DE ERROR DE LA APLICACION
def error(request):
    redirect_to = None
    try:
        redirect_to = request.REQUEST.get('next', '')
    except request.REQUEST.DoesNotExist:
        redirect_to = None

    ctx = {'redirect_to':redirect_to}

    return render_to_response('error.html',ctx,context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=["Administradores","Camareros","Runners","Cocina","Bar"]).count() > 0, login_url='/error/')
def fail(request):
    ctx = {}

    return render_to_response('webapp/fail.html',ctx,context_instance=RequestContext(request))

@login_required()
def perfil(request):
    perfil = Perfil.objects.get(user=request.user)

    ctx = {}
    return render_to_response('webapp/perfil.html', ctx, context_instance=RequestContext(request))

@login_required()
def actualizar_usuario(request):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST,instance=request.user.perfil)
        if perfil_form.is_valid():
            perfil_form.save()
            return HttpResponseRedirect('/perfil')
    else:
        perfil_form = PerfilForm(instance=request.user.perfil) 

    ctx = {'perfil_form':perfil_form}
    return render_to_response('webapp/actualizar_usuario.html',ctx,context_instance=RequestContext(request))

@login_required
def actualizar_password(request):
    if request.method=='POST':
        formulario =  PasswordChangeForm(user=request.user,data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/perfil")    
    else:
        formulario =  PasswordChangeForm(user=request.user)
    
    ctx = {'formulario':formulario}
    return render_to_response('webapp/actualizar_password.html',ctx,context_instance=RequestContext(request))

@login_required()
def actualizar_foto(request):
    if request.method == 'POST':
        foto_form = FotoForm(request.POST,request.FILES,instance=request.user.perfil)
        if foto_form.is_valid():
            foto_form.save()
            return HttpResponseRedirect('/perfil')
    else:
        foto_form = FotoForm(request.POST,instance=request.user.perfil)

    ctx = {'foto_form':foto_form}
    return render_to_response('webapp/actualizar_foto.html',ctx,context_instance=RequestContext(request))

@login_required()
def compras(request):
    if request.user.groups.filter(name="Supervisores"):
        compras = Compra.objects.all().order_by('-id')
    else:
        compras = Compra.objects.filter(usuario=request.user).order_by('-id')

    ctx = {'compras':compras}
    return render_to_response('webapp/compras.html',ctx,context_instance=RequestContext(request))

@login_required()
def movimientos(request):
    movimientos = Transferencia.objects.filter(cuenta__user=request.user).order_by('-id')

    ctx = {'movimientos':movimientos}
    return render_to_response('webapp/movimientos.html',ctx,context_instance=RequestContext(request))

@login_required()
def depositos(request):
    if request.user.groups.filter(name="Supervisores"):
        depositos = Deposito.objects.all().order_by('-id')
    else:
        depositos = Deposito.objects.filter(usuario=request.user).order_by('-id')

    ctx = {'depositos':depositos}
    return render_to_response('webapp/depositos.html',ctx,context_instance=RequestContext(request))

@login_required()
def detalle_compra(request,id_compra):
    compra = Compra.objects.get(id=id_compra)
    compraimpuesto = round(compra.preciototal *  Decimal(0.13),2)
    compraenvio = round(compra.preciototal *  Decimal(0.05),2)
    compratotal = round(Decimal(compraenvio) + Decimal(compraimpuesto) + compra.preciototal,2)

    ctx = {'compra':compra,'compraimpuesto':compraimpuesto,'compraenvio':compraenvio,'compratotal':compratotal}
    return render_to_response('webapp/detalle_compra.html',ctx,context_instance=RequestContext(request))

@login_required()
def detalle_deposito(request,id_deposito):
    deposito = Deposito.objects.get(id=id_deposito)

    ctx = {'deposito':deposito,}
    return render_to_response('webapp/detalle_deposito.html',ctx,context_instance=RequestContext(request))

@login_required()
def imprimir_compra(request,id_compra):
    compra = Compra.objects.get(id=id_compra)

    ctx = {'compra':compra,}
    return render_to_response('webapp/imprimir_compra.html',ctx,context_instance=RequestContext(request))


#VISTA PARA LA CREACION DE UN USUARIO
def nuevo_usuario(request):
    correo=""
    info_enviado = None
    if request.method=='POST':
        formulario_user = UserCreationForm(request.POST)

        if formulario_user.is_valid():
            correo=formulario_user.cleaned_data['email']
            user = formulario_user.save()
            user.is_active = False
            user.save()

            rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
            miserie = rand_str(15)  
            serial = Serial.objects.create(codigo=miserie,email=correo)

            site = Site.objects.get_current()
            email_asunto = "Activar su nueva cuenta"
            email_mensaje = (u"<p> <b> Bienvenido a EffexCard </b>.</p><br><p>Para empezar a utilizar su cuenta EffexCard, solo tiene que confirmar su dirección de correo electrónico.</p><p><a href='http://%s/activar/%s' style='background: #4E9CAF;text-align: center;border-radius: 5px;color: white;font-weight: bold;'>Confirmar mi dirección de correo electrónico</a)></p>"%(site.domain,miserie)).encode("utf8")
            email_texto = "Bienvenido a EffexCard, /n Para empezar a utilizar su cuenta EffexCard, solo tiene que confirmar su direccion de correo electronico. /n <a href='http://%s/activar/%s'></a>"%(site.domain,miserie)
            #configuracion del envio de correo
            msg=EmailMultiAlternatives(email_asunto,email_texto,'EffexCard <donotreply@effexcard.com>',[correo])
            msg.attach_alternative(email_mensaje,'text/html')
            msg.send()

            perfil = Perfil(user=user,fecha_nacimiento=date(1990, 1, 1,), foto="foto_perfil/defaultprofile.jpg")
            perfil.save()
            cuenta = Cuenta(user=user,)
            cuenta.save()
            info_enviado = True
            
        else:
            info_enviado = False
    else:
        formulario_user = UserCreationForm()
        info_enviado = False

    return render_to_response('nuevousuario.html',{'formulario_user':formulario_user,'info_enviado':info_enviado},context_instance=RequestContext(request))

@login_required()
def actualizar_correo(request):
    info = False
    if request.method == 'POST':
        correo_form = CorreoForm(request.POST)
        if correo_form.is_valid():
            correo=correo_form.cleaned_data['email']
            print correo

            rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
            miserie = rand_str(15)  
            serialcorreo = Serialcorreo.objects.create(usuario=request.user,codigo=miserie,email=correo)
            site = Site.objects.get_current()
            email_asunto = "Cambio de Correo Electronico"
            email_mensaje = (u"<p> <b> Saludos desde EffexCard </b>.</p><br><p>Para actualizar su correo electronico asociado a EffexCard, tiene que confirmar su dirección de correo electrónico actual.</p><p><a href='http://%s/activarcorreo/%s' style='background: #4E9CAF;text-align: center;border-radius: 5px;color: white;font-weight: bold;'>Confirmar mi dirección de correo electrónico</a)></p>"%(site.domain,miserie)).encode("utf8")
            email_texto = "Saludos desde EffexCard, /n Para actualizar su correo electronico asociado a EffexCard, tiene que confirmar su direccion de correo electronico actual. /n <a href='http://%s/activarcorreo/%s'></a>"%(site.domain,miserie)

            msg=EmailMultiAlternatives(email_asunto,email_texto,'EffexCard <donotreply@effexcard.com>',[correo])
            msg.attach_alternative(email_mensaje,'text/html')
            msg.send()

            info = True 
    else:
        correo_form = CorreoForm()
        info = False

    ctx = {'correo_form':correo_form,'info':info}
    return render_to_response('webapp/actualizar_correo.html',ctx,context_instance=RequestContext(request))

def activar_cuenta(request,serie):
    try:
        miserie = Serial.objects.get(codigo=serie,valido=True)
    except Serial.DoesNotExist:
        miserie = None
    info = ""
    if miserie:
        miserie.valido = False
        usuario = get_user_model().objects.get(email=miserie.email)
        usuario.is_active = True
        usuario.save()
        info = "Su cuenta ha sido activada"
    else:
        info = "El link ya no es valido, la cuenta ya fue activada."

    ctx = {'info':info,}
    return render_to_response('informacion.html',ctx,context_instance=RequestContext(request))

def activar_correo(request,seriecorreo):
    try:
        miseriecorreo = Serialcorreo.objects.get(codigo=seriecorreo,valido=True)
    except Serialcorreo.DoesNotExist: 
        miseriecorreo = None

    print miseriecorreo.email
    info = ""
    if miseriecorreo:
        miseriecorreo.valido = False
        usuario = get_user_model().objects.get(id=miseriecorreo.usuario.id)
        usuario.email = miseriecorreo.email
        usuario.save()
        info = "Su correo ya ha sido activado"
    else:
        info = "El link ya no es valido."

    ctx = {'info':info,}
    return render_to_response('informacion.html',ctx,context_instance=RequestContext(request))

@login_required()
def agregar_compra(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == 'POST':
        form = CompraForm(request.POST, user = request.user) 
        if form.is_valid():
            registro = form.save()
            if not redirect_to:
                redirect_to = form.cleaned_data['hidden_redirect']
            return HttpResponseRedirect(redirect_to)
        else:
            if not redirect_to:
                redirect_to = form.data['hidden_redirect']
            form.fields['usuario'].widget = forms.HiddenInput()
            form.fields['estado'].widget = forms.HiddenInput()

    else:
        form = CompraForm(user=request.user,initial={'hidden_redirect':redirect_to,'usuario':request.user,'estado':"Pendiente"})
        form.fields['usuario'].widget = forms.HiddenInput()
        form.fields['estado'].widget = forms.HiddenInput()

    ctx = {'form':form,'redirect_to':redirect_to}
    return render_to_response('webapp/nuevo_compra.html',ctx,context_instance=RequestContext(request))

@login_required()
def agregar_compra_externa(request):
    redirect_to = request.REQUEST.get('next', '')
    producto = request.REQUEST.get('producto', '')
    precio = request.REQUEST.get('precio', '')
    cantidad = 1
    descripcion = request.REQUEST.get('descripcion', '')
    tienda = request.REQUEST.get('tienda', '')
    url = request.REQUEST.get('url', '')
    estado = "Pendiente"

    cuenta = Cuenta.objects.filter(user=request.user)[0]
    info = True
    compra = Compra.objects.create(usuario=cuenta.user,producto=producto,preciototal=precio,cantidad=cantidad,descripcion=descripcion,tienda=tienda,direccionurl=url,estado=estado) 
    

    correo="test@effexcard.com"

    site = Site.objects.get_current()
    email_asunto = "Nueva compra por EffexCard"
    email_mensaje = (u"<p> <b> Saludos desde EffexCard, </b></p><br><p>Un usuario acaba de realizar una compra con los siguientes datos: </p><p>Cliente: %s<br>Producto: %s<br>Precio: %s<br>Cantidad: %d</p>"%(request.user.perfil.nombre,producto,precio,cantidad)).encode("utf8")
    email_texto = "Saludos desde EffexCard, /n Un usuario acaba de realizar una compra. </a>"
    #configuracion del envio de correo
    msg=EmailMultiAlternatives(email_asunto,email_texto,'EffexCard <donotreply@effexcard.com>',[correo])
    msg.attach_alternative(email_mensaje,'text/html')
    msg.send()

    ctx = {'info':info,}
    return render_to_response('webapp/nuevo_compra_externa.html',ctx,context_instance=RequestContext(request))


@login_required()
def agregar_deposito(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == 'POST':
        form = DepositoForm(request.POST, request.FILES) 
        if form.is_valid():
            registro = form.save()
            if not redirect_to:
                redirect_to = form.cleaned_data['hidden_redirect']
            return HttpResponseRedirect(redirect_to)
        else:
            if not redirect_to:
                redirect_to = form.data['hidden_redirect']
            form.fields['usuario'].widget = forms.HiddenInput()
            form.fields['estado'].widget = forms.HiddenInput()

    else:
        form = DepositoForm(initial={'hidden_redirect':redirect_to,'usuario':request.user,'estado':"Pendiente"})
        form.fields['usuario'].widget = forms.HiddenInput()
        form.fields['estado'].widget = forms.HiddenInput()

    ctx = {'form':form,'redirect_to':redirect_to}
    return render_to_response('webapp/nuevo_deposito.html',ctx,context_instance=RequestContext(request))

@login_required()
def actualizar_compra(request,operacion,id_compra):
    
    compra = Compra.objects.get(id=id_compra)

    if operacion == "2":
        compra.estado = "Cancelado"
        compra.save()

    if operacion == "3":
        lacuenta = Cuenta.objects.filter(user=compra.usuario)[0]
        if compra.preciototal <= lacuenta.saldo:
            compra.estado = "Aceptado"
            lacuenta.saldo = lacuenta.saldo - compra.preciototal
            transferencia = Transferencia.objects.create(monto=compra.preciototal,detalle="Compra de producto, %s - %s"%(compra.producto,compra.tienda),tipo="salida",responsable=request.user,cuenta=lacuenta,codigo=compra.id)
            lacuenta.save()
        compra.save()
        correo="test@effexcard.com"
        site = Site.objects.get_current()
        email_asunto = "Cambio de estado compra EffexCard"
        email_mensaje = (u"<p> Saludos desde EffexCard, </p><br><p>La compra con ID %s acaba de ser actualizada al estado: %s </p>"%(compra.id,compra.estado)).encode("utf8")
        email_texto = "Saludos desde EffexCard, /n La compra con ID acaba de ser actualizada "
        #configuracion del envio de correo
        msg=EmailMultiAlternatives(email_asunto,email_texto,'EffexCard <donotreply@effexcard.com>',[correo])
        msg.attach_alternative(email_mensaje,'text/html')
        msg.send()

            
    if operacion == "4":
        compra.estado = "Rechazado"
        compra.save()

 
    redirect_to = request.REQUEST.get('next', '')

    return HttpResponseRedirect(redirect_to)

@login_required()
def actualizar_deposito(request,operacion,id_deposito):
    
    deposito = Deposito.objects.get(id=id_deposito)

    if operacion == "2":
        compra.estado = "Cancelado"

    if operacion == "3":
        lacuenta = Cuenta.objects.filter(user=deposito.usuario)[0]
        deposito.estado = "Aceptado"
        lacuenta.saldo = lacuenta.saldo + deposito.monto
        transferencia = Transferencia.objects.create(monto=deposito.monto,detalle="Depósito",tipo="entrada",responsable=request.user,cuenta=lacuenta,codigo=deposito.id)
        lacuenta.save()

        correo="test@effexcard.com"
        site = Site.objects.get_current()
        email_asunto = "Deposito Aceptado EffexCard"
        email_mensaje = (u"<p> Saludos desde EffexCard, </p><br><p>El deposito con ID %s acaba de ser aceptado </p>"%(deposito.id,)).encode("utf8")
        email_texto = "Saludos desde EffexCard, /n Su deposito acaba de ser aceptado"
        #configuracion del envio de correo
        msg=EmailMultiAlternatives(email_asunto,email_texto,'EffexCard <donotreply@effexcard.com>',[correo])
        msg.attach_alternative(email_mensaje,'text/html')
        msg.send()

    if operacion == "4":
        deposito.estado = "Rechazado"

    deposito.save()
    redirect_to = request.REQUEST.get('next', '')

    return HttpResponseRedirect(redirect_to)