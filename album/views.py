# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse 
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from album.serializers import CategorySerializer, PhotoSerializer
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.conf import settings
from datetime import date
from django.template import context
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from album.forms import PostForm
from album.models import models
from django.db.models import Q
from models import Egresado, Facultad, Programa, Modalidad, TipoPago
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
# Create your views here.
d = date.today()
#for a 
global results
global query
results=""
query=""

class PhotoUpdate(UpdateView):
 login_required = True
 model = Photo
 fields = '__all__'

class PhotoCreate(CreateView):
 login_required = True
 model = Photo 
 fields = '__all__'

class PhotoDelete(DeleteView):
 login_required = True
 model = Photo
 success_url = reverse_lazy('photo-list')

class CategoryCreate(CreateView):
 login_required = True
 model = Category 
 fields = '__all__'

class CategoryDelete(DeleteView):
 login_required = True
 model = Category
 success_url = reverse_lazy('category-list')

class CertificadoEgresadoPDF(View):
    def cabecera(self,pdf):
    #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/photos/logo.png'
        firma_imagen =(settings.MEDIA_ROOT+'/photos/firma.PNG')
    #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 30, 720, 110, 90,preserveAspectRatio=True)
        pdf.drawImage(firma_imagen, 200, 246, 250, 110,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
    #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"UNIVERSIDAD MARIANA")
        pdf.drawString(180, 770, u"REGISTRO Y CONTROL ACADEMICO")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(225, 750, u"CERTIFICADO PARA EGRESADOS")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(260, 680, u"HACE CONSTAR:")
        pdf.drawString(60, 630, u"Que el(la) señor(a)"+str(self.buscar(pdf))+" identificado(a) con cedula de ciudadanía No.")
        pdf.drawString(60, 615, u"_________"+" es egresado del curso de pregrado "+"______________"+" de la") 
        pdf.drawString(60, 600, u"Universidad Mariana el "+"__________")
        pdf.drawString(60, 550, u"La universidad Mariana identificada con Nit. NO 800.092.198-5 es una") 
        pdf.drawString(60, 535, u"institución de educación superior reconocida como tal por el Articulo 137 de la") 
        pdf.drawString(60, 520, u"ley 30 de 1992, Ley de Educación Superior. Se expide la presente constancia a") 
        pdf.drawString(60, 505, u"solicitud del interesado el "+d.strftime("%d %B %Y"))
        pdf.drawString(200, 245,u"HNA. AMANDA LUCERO VALLEJO")
        pdf.drawString(220, 225,u"Rectora Universidad Mariana")
        
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        self.buscar(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def buscar(self,pdf):
        results=[(egresado.nombre, egresado.apellido) for egresado in Egresado.objects.filter()]

class EgresadoList(ListView):
    model = Egresado

@login_required
def base(request):
    return render(request , "base.html")

@login_required
def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request,'album/category.html', context)

@login_required
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request,'album/category_detail.html', context)

@login_required
def LogOut(request):
    logout(request)
    return redirect('/accounts/login')

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


def Formulario(request):
    return render(request,'album/formulario_egresado.html')

def buscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(numero_documento=query)
        )
        results = Egresado.objects.filter(qset)
    else:
        results = []
        #results = Q(numero_documento=query) 
    return render_to_response("album/buscar.html", {"results": results,"query": query})
    
#clases para el egresado   
    
class EgresadoCreate(CreateView):
    model = Egresado
    fields = '__all__'
    template_name='album/egresado_form.html'

    @method_decorator(permission_required('egresado.egresado-create',reverse_lazy('egresado:egresado')))
    def dispatch(self, *args, **kwargs):
        return super(EgresadoCreate, self).dispatch(*args, **kwargs)

class EgresadoDelete(DeleteView):
    login_required = True
    model = Egresado
    fields = '__all__'
    success_url = reverse_lazy('egresado-list') 

    @method_decorator(permission_required('egresado.egresado-delete',reverse_lazy('egresado:egresado')))
    def dispatch(self, *args, **kwargs):
        return super(EgresadoDelete, self).dispatch(*args, **kwargs)

class EgresadoUpdate(UpdateView):
    login_required = True
    model = Egresado
    fields = '__all__'
    success_url = reverse_lazy('egresado-list')

    @method_decorator(permission_required('egresado.egresado-update',reverse_lazy('egresado:egresado')))
    def dispatch(self, *args, **kwargs):
        return super(EgresadoUpdate, self).dispatch(*args, **kwargs)


@login_required
def egresado_list(request):
    egresado_list = Egresado.objects.all()
    context = {'object_list': egresado_list}
    template_name='album/egresado_detail.html'
    return render(request,'album/lista_egresados.html', context)

@login_required
def egresado_detail(request, id_egresado):
    egresado = Egresado.objects.get(id_egresado=id_egresado)
    context = {'object': egresado}
    return render(request,'album/egresado_detail.html', context)


#clases para la facultad
class FacultadCreate(CreateView):
    model = Facultad
    fields = '__all__'
    template_name='album/facultad_form.html'

    @method_decorator(permission_required('facultad.facultad-create',reverse_lazy('facultad:facultad')))
    def dispatch(self, *args, **kwargs):
        return super(FacultadCreate, self).dispatch(*args, **kwargs)

class FacultadDelete(DeleteView):
    login_required = True
    model = Facultad
    fields = '__all__'
    success_url = reverse_lazy('facultad-list') 

    @method_decorator(permission_required('facultad.facultad-delete',reverse_lazy('facultad:facultad')))
    def dispatch(self, *args, **kwargs):
        return super(FacultadDelete, self).dispatch(*args, **kwargs)

class FacultadUpdate(UpdateView):
    login_required = True
    model = Facultad
    fields = '__all__'
    success_url = reverse_lazy('facultad-list')

    @method_decorator(permission_required('facultad.facultad-update',reverse_lazy('facultad:facultad')))
    def dispatch(self, *args, **kwargs):
        return super(FacultadUpdate, self).dispatch(*args, **kwargs)

@login_required
def facultad_list(request):
    facultad_list = Facultad.objects.all()
    context = {'object_list': facultad_list}
    template_name='album/facultad_detail.html'
    return render(request,'album/facultad_list.html', context)

@login_required
def facultad_detail(request, id_facultad):
    facultad = Facultad.objects.get(id_facultad=id_facultad)
    context = {'object': facultad}
    return render(request,'album/facultad_detail.html', context)

#clases para la programa
class ProgramaCreate(CreateView):
    model = Programa
    fields = '__all__'
    template_name='album/programa_form.html'

    @method_decorator(permission_required('programa.programa-create',reverse_lazy('programa:programa')))
    def dispatch(self, *args, **kwargs):
        return super(ProgramaCreate, self).dispatch(*args, **kwargs)

class ProgramaDelete(DeleteView):
    login_required = True
    model = Programa
    fields = '__all__'
    success_url = reverse_lazy('programa-list') 

    @method_decorator(permission_required('programa.programa-delete',reverse_lazy('programa:programa')))
    def dispatch(self, *args, **kwargs):
        return super(ProgramaDelete, self).dispatch(*args, **kwargs)

class ProgramaUpdate(UpdateView):
    login_required = True
    model = Programa
    fields = '__all__'
    success_url = reverse_lazy('programa-list')

    @method_decorator(permission_required('programa.programa-update',reverse_lazy('programa:programa')))
    def dispatch(self, *args, **kwargs):
        return super(ProgramaUpdate, self).dispatch(*args, **kwargs)

@login_required
def programa_list(request):
    programa_list = Programa.objects.all()
    context = {'object_list': programa_list}
    template_name='album/programa_detail.html'
    return render(request,'album/programa_list.html', context)

@login_required
def programa_detail(request, id_programa):
    programa = Programa.objects.get(id_programa=id_programa)
    context = {'object': programa}
    return render(request,'album/programa_detail.html', context)

#clases para la modalidad
class ModalidadCreate(CreateView):
    model = Modalidad
    fields = '__all__'
    template_name='album/modalidad_form.html'

    @method_decorator(permission_required('modalidad.modalidad-create',reverse_lazy('modalidad:modalidad')))
    def dispatch(self, *args, **kwargs):
        return super(ModalidadCreate, self).dispatch(*args, **kwargs)

class ModalidadDelete(DeleteView):
    login_required = True
    model = Modalidad
    fields = '__all__'
    success_url = reverse_lazy('modalidad-list') 

    @method_decorator(permission_required('modalidad.modalidad-delete',reverse_lazy('modalidad:modalidad')))
    def dispatch(self, *args, **kwargs):
        return super(ModalidadDelete, self).dispatch(*args, **kwargs)

class ModalidadUpdate(UpdateView):
    login_required = True
    model = Modalidad
    fields = '__all__'
    success_url = reverse_lazy('modalidad-list')

    @method_decorator(permission_required('modalidad.modalidad-update',reverse_lazy('modalidad:modalidad')))
    def dispatch(self, *args, **kwargs):
        return super(ModalidadUpdate, self).dispatch(*args, **kwargs)

@login_required
def modalidad_list(request):
    modalidad_list = Modalidad.objects.all()
    context = {'object_list': modalidad_list}
    template_name='album/modalidad_detail.html'
    return render(request,'album/modalidad_list.html', context)

@login_required
def modalidad_detail(request, id_modalidad):
    modalidad = Modalidad.objects.get(id_modalidad=id_modalidad)
    context = {'object': modalidad}
    return render(request,'album/modalidad_detail.html', context)


#clases para la tipo pago
class Tipo_pagoCreate(CreateView):
    model = TipoPago
    fields = '__all__'
    template_name='album/tipopago_form.html'

    @method_decorator(permission_required('tipo_pago.tipo_pago-create',reverse_lazy('tipo_pago:tipo_pago')))
    def dispatch(self, *args, **kwargs):
        return super(Tipo_pagoCreate, self).dispatch(*args, **kwargs)

class Tipo_pagoDelete(DeleteView):
    login_required = True
    model = TipoPago
    fields = '__all__'
    success_url = reverse_lazy('tipo_pago-list') 

    @method_decorator(permission_required('tipo_pago.tipo_pago-delete',reverse_lazy('tipo_pago:tipo_pago')))
    def dispatch(self, *args, **kwargs):
        return super(Tipo_pagoDelete, self).dispatch(*args, **kwargs)

class Tipo_pagoUpdate(UpdateView):
    login_required = True
    model = TipoPago
    fields = '__all__'
    success_url = reverse_lazy('tipo_pago-list')

    @method_decorator(permission_required('tipo_pago.tipo_pago-update',reverse_lazy('tipo_pago:tipo_pago')))
    def dispatch(self, *args, **kwargs):
        return super(Tipo_pagoUpdate, self).dispatch(*args, **kwargs)

@login_required
def tipo_pago_list(request):
    tipo_pago_list = TipoPago.objects.all()
    context = {'object_list': tipo_pago_list}
    template_name='album/tipopago_detail.html'
    return render(request,'album/tipopago_list.html', context)

@login_required
def tipo_pago_detail(request, id_tipo_pago):
    tipo_pago = TipoPago.objects.get(id_tipo_pago=id_tipo_pago)
    context = {'object': tipo_pago}
    return render(request,'album/tipopago_detail.html', context)
