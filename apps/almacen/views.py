from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class Index(LoginRequiredMixin, View):

    template_name = 'almacen/index.html'
    def get(self, request):
        return render(request, self.template_name)

class Operaciones(LoginRequiredMixin,View):
    template_name='almacen/operaciones/index.html'
    def get(self,request):
        return render(request,self.template_name)

class Ingresos(LoginRequiredMixin,View):
    template_name='almacen/ingresos/index.html'
    def get(self,request):
        return render(request,self.template_name)

class Reingresos(LoginRequiredMixin,View):
    template_name='almacen/reingresos/index.html'
    def get(self,request):
        return render(request,self.template_name)

class Salidas(LoginRequiredMixin,View):
    template_name='almacen/salidas/index.html'
    def get(self,request):
        return render(request,self.template_name)