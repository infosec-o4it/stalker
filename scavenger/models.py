# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.


class TipoContacto(models.Model):
    """(TipoContacto description)"""
    """ Modelo usado para almacenar los posibles tipos de contacto de un cliente
    para su uso en la labor comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Tipos de Contacto"
        verbose_name = "Tipo de Contacto"

    def __unicode__(self):
        return u"Contacto Tipo %s" % (self.Nombre)


class ClienteEntidad(models.Model):
    """(ClienteEntidad descripcion)"""
    """ Modelo usado para almacenar los posbles clientes o entidades a futuro
    se puedan obtener o concretar para la labor comercial """
    Nombre = models.CharField(max_length=100)
    TipoContacto = models.ForeignKey(TipoContacto,
                                     verbose_name='Tipo de Contacto')
    NombreContacto = models.CharField(blank=True, max_length=100,
                                      verbose_name='Nombre del Contacto')
    DatosContacto = models.CharField(blank=True, max_length=100,
                                     verbose_name='Datos del Contacto')

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'NombreContacto', 'DatosContacto',)
        search_fields = ('Nombre', 'NombreContacto',)

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def __unicode__(self):
        return u"Cliente %s" % (self.Nombre)


class RolServidor(models.Model):
    """(RolServidor description)"""
    """ Modelo Usado para almacenar los posibles roles a futuro que se puedan
    vender o obtener para la labor comercial """
    Nombre = models.CharField(max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Roles de Servidor"
        verbose_name = "Rol de Servidor"

    def __unicode__(self):
        return u"Rol %s" % (self.Nombre)

"""Tupla usada para almcenar los tipos de servidor del cliente"""
EleccionesTipoServidor = (
    ('HW', 'Fisico'),
    ('VM', 'Virutalizado'),
)


class VirtualizadorServidor(models.Model):
    """(VirtualizadorServidor description)"""
    """ Modelo usado para almacenar los tipos de virtualizador que esta usando
    una maquina virtual del cliente (valor opcional) """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Tipos de Virtualizador"
        verbose_name = "Tipo de Virtualizador"

    def __unicode__(self):
        return u"Virtualizador Tipos %s" % (self.Nombre)


class SistemaOperativo(models.Model):
    """(SistemaOperativo description)"""
    """ Modelo usado para almacenar los posibles tipos de sistemas operativos
    de los servidores del cliente para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Sistemas Operativos"
        verbose_name = "Sistema Operativo"

    def __unicode__(self):
        return u"Sistema Operativo %s" % (self.Nombre)


class ArquitecturaServidor(models.Model):
    """(ArquitecturaServidor descripcion)"""
    """ Modelo usado para almecenar los posibles tipos de arquitecturas del los
    posibles servidores del cliente para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Arquitecturas de Servidor"
        verbose_name = "Arquitectura de Servidor"

    def __unicode__(self):
        return u"Arquitectura %s" % (self.Nombre)


class TipoDb(models.Model):
    """(TipoDB descripcion)"""
    """ modelo usado para almacenar los posibles tipos de bases de datos que
    que emplea el cliente en su servidor , informacion usada para uso comercial
    """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Tipos de DB"
        verbose_name = "Tipo de DB"

    def __unicode__(self):
        return u"Base de datos tipo %s" % (self.Nombre)


class TipoClusterdb(models.Model):
    """(TipoClusterdb description)"""
    """ Modelo usado para almacenar los posibles tipos de cluster que usan las
    bases de datos que el cliente usa, informacion almacenada para uso
    comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Tipos de Cluster"
        verbose_name = "Tipo de Cluster"

    def __unicode__(self):
        return u"Tipo Cluster %s" % (self.Nombre)


class VersionDB(models.Model):
    """(VersionDB description)"""
    """modelo usado para almacenar de manera relacionada las la version de Base
    de datos usada por el cliente"""
    Version = models.CharField(blank=True, max_length=100)
    Tipo_Db = models.ForeignKey(TipoDb)

    class Admin(admin.ModelAdmin):
        list_display = ('Version', 'Tipo_Db')
        search_fields = ('Version',)

    class Meta:
        verbose_name_plural = "Versiones de DB"
        verbose_name = "Version de DB"

    def __unicode__(self):
        return u"%s Version %s" % (str(self.Tipo_Db), self.Version)


class TipoAplicacion(models.Model):
    """(TipoAplicacion description)"""
    """ Modelo usado para almacenar los tipos de servidores de aplicacion que
    el cliente quiere o tiene, informacion almacenada para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Tipos de Aplicaccón"
        verbose_name = "Tipo de Aplicación"

    def __unicode__(self):
        return u"Tipo Servidor Aplicacion %s" % (self.Nombre)


class EsquemaLicenciamiento(models.Model):
    """(EsquemaLicenciamiento description)"""
    """ Modelo usado para almacenar el esquema de licenciamiento de un servidor
    de aplicacion o base de datos que usa el cliente o quiere usar, informacion
    almacenada para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Esquemas de licenciamiento"
        verbose_name = "Esquema de licenciamiento"

    def __unicode__(self):
        return u" %s " % (self.Nombre)


class ServidorEntidad(models.Model):
    """(ServidorEntidad description)"""
    """ Modelo usado para almacenar de manera realacionda informacion que el
    cliente proporcione de sus servidores, informacion almacenada para posible
    uso comercial """
    Cliente = models.ForeignKey(ClienteEntidad)
    Rol = models.ForeignKey(RolServidor)
    Tipo = models.CharField(blank=True, max_length=100,
                            choices=EleccionesTipoServidor)
    Virtualizador = models.ForeignKey(VirtualizadorServidor, blank=True,
                                      null=True)
    Sistema_Operativo = models.ForeignKey(SistemaOperativo)
    Arquitectura = models.ForeignKey(ArquitecturaServidor)
    No_Nucleos_CPU = models.IntegerField(blank=True, null=True)
    Uso_CPU = models.FloatField(blank=True, null=True)
    Ram = models.IntegerField(blank=True, null=True)
    Uso_Ram = models.FloatField(blank=True, null=True)
    Uso_Disco = models.IntegerField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Cliente', 'No_Nucleos_CPU', 'Ram')
        search_fields = ('Cliente__Nombre',)

    class Meta:
        verbose_name_plural = "Servidores de Cliente"
        verbose_name = "Servidor de Cliente"

    def __unicode__(self):
        return u"Servidor de %s Cpu #%s Ram #%s" % (self.Cliente,
                                                    self.No_Nucleos_CPU,
                                                    self.Ram)


class ServidorTipoDB(models.Model):
    """(ServidorTipoDB description)"""
    """ modelo usado para almacenar de manera relacionadas los datos de los
    servidores de cliente que sean tipo base de datos """
    Cliente = models.ForeignKey(ClienteEntidad)
    # Tipo = models.ForeignKey(TipoDb)
    Version = models.ForeignKey(VersionDB)
    Velocidad_Transferencia = models.CharField(blank=True, max_length=100)
    Cluster = models.NullBooleanField(blank=True)
    Tipo_Cluster = models.ForeignKey(TipoClusterdb, blank=True, null=True)
    Mirroring = models.NullBooleanField(blank=True)
    Replica = models.NullBooleanField(blank=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Cliente', 'Version', )
        search_fields = ('Cliente__Nombre',)

    class Meta:
        verbose_name_plural = "Servidores de DB del cliente"
        verbose_name = "Servidor DB del cliente"

    def __unicode__(self):
        return u"Servidor de Base de Datos Cliente %s %s" % (self.Cliente,
                                                             self.Version)


class ServidorAplicacion(models.Model):
    """(ServidorAplicacion description)"""
    """modelo usado para almacenar los diferentes tipos de servidores de
    aplicacion que el cliente tiene o necesita """
    Cliente = models.ForeignKey(ClienteEntidad)
    Tipo = models.ForeignKey(TipoAplicacion)
    Usuarios_Concurrentes = models.CharField(blank=True, max_length=100)
    Esquema_licenciamiento = models.ForeignKey(EsquemaLicenciamiento,
                                               blank=True)
    RTO = models.CharField(blank=True, max_length=100)
    RPO = models.CharField(blank=True, max_length=100)
    Periodicidad_Backups = models.IntegerField(blank=True, null=True)
    Retencion_Backups = models.IntegerField(blank=True, null=True)
    Test_Backups = models.NullBooleanField(blank=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Cliente', 'Tipo',)
        search_fields = ('Cliente__Nombre',)

    class Meta:
        verbose_name_plural = "Saas del Cliente"
        verbose_name = "Servidores de aplicacion del Cliente"

    def __unicode__(self):
        return u"Servidor de Aplicacion Cliente %s Tipo %s" % (self.Cliente,
                                                               self.Tipo)


class TipoEnlace(models.Model):
    """(TipoEnlace description)"""
    """ modelo usado para almacenar los posibles tipos de enlace que tenga la
    topologia(s) de un cliente, infomacion almacenada para uso comercial"""
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('',)

    class Meta:
        verbose_name_plural = "Tipos de Enlace"
        verbose_name = "Tipo de Enlace"

    def __unicode__(self):
        return u"Tipo de Enlace %s" % (self.Nombre)


class IspTopologia(models.Model):
    """(IspTopologia description)"""
    """ modelo usado para almacenar los posibles proveedores de internet de
    las topologias de los clientes, informacion almacenada para posible uso
    comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('',)

    class Meta:
        verbose_name_plural = "Isp's"
        verbose_name = "Proveedor de Internet"

    def __unicode__(self):
        return u"Isp %s" % (self.Nombre)


class TipoAlmacenamiento(models.Model):
    """(TipoAlmacenamiento description)"""
    """ modelo usado para almacenar los posibles tipos de almacenamientos
    implementados que usa una topologia de un cliente, informacion almacenada
    para posible uso comercial """
    Tipo_Disco = models.CharField(blank=True, max_length=100)
    Tipo_Storage = models.CharField(blank=True, max_length=100)
    Tipo_Conexion = models.CharField(blank=True, max_length=100)
    Velocidad = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Tipo_Disco', 'Tipo_Storage',)
        search_fields = ('',)

    class Meta:
        verbose_name_plural = "Tipos de Almacenamiento"
        verbose_name = "Tipo de Almacenamiento"

    def __unicode__(self):
        return u"%s - %s - %s - %s" % (self.Tipo_Conexion, self.Tipo_Disco,
                                       self.Tipo_Storage, self.Velocidad)


class TopologiaEntidad(models.Model):
    """(TopologiaEntidad description)"""
    """ Modelo usado para almacenar datos de la topologia del cliente, para
    posible uso comercial"""
    Cliente = models.ForeignKey(ClienteEntidad)
    Ubicacion = models.CharField(blank=True, max_length=100)
    Cantidad_Servidores = models.IntegerField(blank=True, null=True)
    Tipo_Enlace = models.ForeignKey(TipoEnlace, blank=True)
    Ancho_Banda = models.CharField(blank=True, max_length=100)
    Isp = models.ForeignKey(IspTopologia, blank=True)
    Tipo_Almacenamiento = models.ForeignKey(TipoAlmacenamiento, blank=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Cliente', 'Cantidad_Servidores', 'Ubicacion')
        search_fields = ('',)

    class Meta:
        verbose_name_plural = "Topogias de Clientes"
        verbose_name = "Topologia de Cliente"

    def __unicode__(self):
        return u"Topologia %s %s %s" % (self.Cliente, self.Cantidad_Servidores,
                                        self.Ubicacion)
