# coding: utf-8
# ARCHIVO PARA LA CONFIGURACION DE LAS URL
from django.conf.urls import patterns, include, url
from webapp.views import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
import settings

#CONFIGURACION DE URLS DE LA APLICACION
urlpatterns = patterns('webapp.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'control_ingreso', name='control_ingreso'),
    url(r'^store/$', 'store', name='store'),
    url(r'^website/$', 'website', name='website'),
    url(r'^quienes_somos/$', 'quienes_somos', name='quienes_somos'),
    url(r'^quiero_negocio/$', 'quiero_negocio', name='quiero_negocio'),
    url(r'^ayuda/$', 'ayuda', name='ayuda'),


    url(r'^login/$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^home/$', "home", name="home"),
    url(r'^error/$', "error", name="error"),
    url(r'^fail/$', "fail", name="fail"),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name="logout"),
    url(r'^signup/$','nuevo_usuario'),
    url(r'^perfil/$', "perfil", name="perfil"),

    url(r'^compras/$', "compras"),
    url(r'^depositos/$', "depositos"),
    url(r'^movimientos/$', "movimientos"),
    
    url(r'^actualizar/usuario/$', "actualizar_usuario", name="actualizar_usuario"),
    url(r'^actualizar/foto/$', "actualizar_foto", name="actualizar_foto"),
    url(r'^actualizar/correo/$', "actualizar_correo", name="actualizar_correo"),
    url(r'^actualizar/password/$', "actualizar_password", name="actualizar_password"),

    url(r'^agregar/compra/$', "agregar_compra", name="agregar_compra"),
    url(r'^agregar/compra/externa/$', "agregar_compra_externa", name="agregar_compra_externa"),
    url(r'^actualizar/compra/(?P<operacion>.*)/(?P<id_compra>.*)/$', "actualizar_compra", name="actualizar_compra"),
    url(r'^detalle/compra/(?P<id_compra>.*)/$', "detalle_compra", name="detalle_compra"),
    url(r'^imprimir/compra/(?P<id_compra>.*)/$', "imprimir_compra", name="imprimir_compra"),
    
    url(r'^agregar/deposito/$', "agregar_deposito"),
    url(r'^actualizar/deposito/(?P<operacion>.*)/(?P<id_deposito>.*)/$', "actualizar_deposito"),
    url(r'^detalle/deposito/(?P<id_deposito>.*)/$', "detalle_deposito"),

    url(r'^activar/(?P<serie>.*)/$', "activar_cuenta", name="activar_cuenta"),
    url(r'^activarcorreo/(?P<seriecorreo>.*)/$', "activar_correo", name="activar_correo"),

)

#URL RECUPERACION CONTRASEÑA
urlpatterns += patterns('',
     url(r'^reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/reset/done'},
        name="password_reset"),
    (r'^reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/login'}),
    (r'^done/$', 
        'django.contrib.auth.views.password_reset_complete'),
)

#CARGA DE MEDIA
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )