#REGISTRO DE TODOS LOS MODELOS EN LA ADMINISTRACION DE LA APLICACION WEB /ADMIN
from django.contrib import admin
from models import * 
# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    list_display   = ('user','celular','direccion')
    ordering = ('user',)
    search_fields = ('user',)

class DepositoAdmin(admin.ModelAdmin):
    list_display   = ('id',)
    ordering = ('id',)


admin.site.register(Perfil,PerfilAdmin)
admin.site.register(Deposito,DepositoAdmin)