# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse 
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from album.serializers import CategorySerializer, PhotoSerializer
# Create your views here.


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