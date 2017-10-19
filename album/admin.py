# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#QUITAR EL ERROR DE CODIFICACION ENTRE UTF-8 Y ASCCI
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin

from album.models import Category, Photo
# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
