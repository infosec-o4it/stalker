from django.contrib import admin
from .models import TipoContacto, ClienteEntidad, RolServidor, TipoDb
from .models import VirtualizadorServidor, SistemaOperativo, TipoClusterdb
from .models import ArquitecturaServidor, VersionDB, TipoAplicacion, TipoEnlace
from .models import EsquemaLicenciamiento, ServidorEntidad, ServidorTipoDB
from .models import ServidorAplicacion, IspTopologia, TipoAlmacenamiento
from .models import TopologiaEntidad
# Register your models here.
admin.site.register(TipoContacto, TipoContacto.Admin)
admin.site.register(ClienteEntidad, ClienteEntidad.Admin)
admin.site.register(RolServidor, RolServidor.Admin)
admin.site.register(TipoDb, TipoDb.Admin)
admin.site.register(VirtualizadorServidor, VirtualizadorServidor.Admin)
admin.site.register(SistemaOperativo, SistemaOperativo.Admin)
admin.site.register(TipoClusterdb, TipoClusterdb.Admin)
admin.site.register(ArquitecturaServidor, ArquitecturaServidor.Admin)
admin.site.register(VersionDB, VersionDB.Admin)
admin.site.register(TipoAplicacion, TipoAplicacion.Admin)
admin.site.register(TipoEnlace, TipoEnlace.Admin)
admin.site.register(EsquemaLicenciamiento, EsquemaLicenciamiento.Admin)
admin.site.register(ServidorEntidad, ServidorEntidad.Admin)
admin.site.register(ServidorTipoDB, ServidorTipoDB.Admin)
admin.site.register(ServidorAplicacion, ServidorAplicacion.Admin)
admin.site.register(IspTopologia, IspTopologia.Admin)
admin.site.register(TipoAlmacenamiento, TipoAlmacenamiento.Admin)
admin.site.register(TopologiaEntidad, TopologiaEntidad.Admin)
