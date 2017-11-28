# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-list')

class Photo(models.Model):
    """ Fotos del album """
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo-list')

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)

class EstadoCivil(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_civil'
    
    def __unicode__(self):
            return self.estado

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultad'

    def __unicode__(self):
            return self.nombre
    
    def get_absolute_url(self):
        return reverse('facultad-list')



class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'
        
    def __unicode__(self):
            return self.tipo


class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'

    def __unicode__(self):
            return self.tipo
    
    def get_absolute_url(self):
        return reverse('modalidad-list')


class Programa(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True, default='nombre')
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa'

    def __unicode__(self):
            return self.nombre
    
    def get_absolute_url(self):
        return reverse('programa-list')

class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_pago'
    
    def __unicode__(self):
            return self.tipo
    
    def get_absolute_url(self):
        return reverse('tipo_pago-list')

class Egresado(models.Model):
    id_egresado = models.AutoField(primary_key=True)
    numero_documento = models.CharField(max_length=300, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    apellido = models.CharField(max_length=300, blank=True, null=True)
    id_programa = models.ForeignKey(Programa, models.DO_NOTHING, db_column='id_programa', blank=True, null=True)
    fecha_inicio = models.CharField(max_length=50, blank=True, null=True)
    fecha_fin = models.CharField(max_length=50, blank=True, null=True)
    id_modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='id_modalidad', blank=True, null=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad', blank=True, null=True)
    estrato = models.CharField(max_length=50, blank=True, null=True)
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero', blank=True, null=True)
    edad = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    id_estado = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_tipo_pago = models.ForeignKey(TipoPago, models.DO_NOTHING, db_column='id_tipo_pago', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'egresado'
       
    def __unicode__(self):
        return unicode(self.nombre)
    
    def get_absolute_url(self):
        return reverse('egresado-list')


    