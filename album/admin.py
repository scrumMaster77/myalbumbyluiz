# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#QUITAR EL ERROR DE CODIFICACION ENTRE UTF-8 Y ASCCI
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin

from album.models import Category, Photo, Egresado, Facultad, Modalidad, TipoPago, Programa, Genero, EstadoCivil
# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Egresado)
admin.site.register(Facultad)
admin.site.register(Modalidad)
admin.site.register(TipoPago)
admin.site.register(Programa)
admin.site.register(Genero)
admin.site.register(EstadoCivil)

