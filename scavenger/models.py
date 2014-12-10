from django.db import models

# Create your models here.


class TipoContacto(models.Model):
    """(TipoContacto description)"""
    """ Modelo usado para almacenar los posibles tipos de contacto de un cliente
    para su uso en la labor comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Contacto Tipo %s" % (self.Nombre)


class ClienteEntidad(models.Model):
    """(ClienteEntidad descripcion)"""
    """ Modelo usado para almacenar los posbles clientes o entidades a futuro
    se puedan obtener o concretar para la labor comercial """
    Nombre = models.CharField(max_length=100)
    TipoContacto = models.ForeignKey(TipoContacto)
    NombreContacto = models.CharField(blank=True, max_length=100)
    DatosContacto = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre', 'NombreContacto', 'DatosContacto',)
        search_fields = ('Nombre', 'NombreContacto',)

    def __unicode__(self):
        return u"Cliente %s" % (self.Nombre)


class RolServidor(models.Model):
    """(RolServidor description)"""
    """ Modelo Usado para almacenar los posibles roles a futuro que se puedan
    vender o obtener para la labor comercial """
    Nombre = models.CharField(max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Rol %s" % (self.Nombre)

EleccionesTipoServidor = (
    """Tupla usada para almcenar los tipos de servidor del cliente"""
    ('HW', 'Fisico'),
    ('VM', 'Virutalizado'),
)


class VirtualizadorServidor(models.Model):
    """(VirtualizadorServidor description)"""
    """ Modelo usado para almacenar los tipos de virtualizador que esta usando
    una maquina virtual del cliente (valor opcional) """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Virtualizador Tipos %s" % (self.Nombre)


class SistemaOperativo(models.Model):
    """(SistemaOperativo description)"""
    """ Modelo usado para almacenar los posibles tipos de sistemas operativos
    de los servidores del cliente para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Sistema Operativo %s" % (self.Nombre)


class ArquitecturaServidor(models.Model):
    """(ArquitecturaServidor descripcion)"""
    """ Modelo usado para almecenar los posibles tipos de arquitecturas del los
    posibles servidores del cliente para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Arquitectura %s" % (self.Nombre)


class TipoDb(models.Model):
    """(TipoDB descripcion)"""
    """ modelo usado para almacenar los posibles tipos de bases de datos que
    que emplea el cliente en su servidor , informacion usada para uso comercial
    """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Base de datos tipo %s" % (self.Nombre)


class TipoClusterdb(models.Model):
    """(TipoClusterdb description)"""
    """ Modelo usado para almacenar los posibles tipos de cluster que usan las
    bases de datos que el cliente usa, informacion almacenada para uso
    comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Tipo Cluster %s" % (slef.Nombre)


class VersionDB(models.Model):
    """(VersionDB description)"""
    """modelo usado para almacenar de manera relacionada las la version de Base
    de datos usada por el cliente"""
    Version = models.CharField(blank=True, max_length=100)
    Tipo_Db = models.ForeignKey(TipoDb)

    class Admin:
        list_display = ('Version', 'Tipo_Db')
        search_fields = ('Version',)

    def __unicode__(self):
        return u"Version %s" % (self.version + " - " + self.Tipo_Db)


class TipoAplicacion(models.Model):
    """(TipoAplicacion description)"""
    """ Modelo usado para almacenar los tipos de servidores de aplicacion que
    el cliente quiere o tiene, informacion almacenada para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u"Tipo Servidor Aplicacion %s" % (self.Nombre)


class EsquemaLicenciamiento(models.Model):
    """(EsquemaLicenciamiento description)"""
    """ Modelo usado para almacenar el esquema de licenciamiento de un servidor
    de aplicacion o base de datos que usa el cliente o quiere usar, informacion
    almacenada para uso comercial """
    Nombre = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    def __unicode__(self):
        return u" %s " % (self.Nombre)


class ServidorEntidad(models.Model):
    """(ServidorEntidad description)"""
    """ Modelo usado para almacenar de manera realacionda informacion que el
    cliente proporcione de sus servidores, informacion almacenada para posible
    uso comercial """
    Cliente = models.ForeignKey(ClienteEntidad)
    Rol = models.ForeignKey(RolServidor)
    Tipo = models.CharField(blank=True, max_length=100)
    Virtualizador = models.ForeignKey(VirtualizadorServidor)
    Sistema_Operativo = models.ForeignKey(SistemaOperativo)
    Arquitectura = models.ForeignKey(ArquitecturaServidor)
    No_Nucleos_CPU = models.IntegerField(blank=True, null=True)
    Uso_CPU = models.FloatField(blank=True, null=True)
    Ram = models.IntegerField(blank=True, null=True)
    Uso_Ram = models.FloatField(blank=True, null=True)
    Uso_Disco = models.IntegerField(blank=True, null=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Servidor"
