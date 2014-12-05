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
