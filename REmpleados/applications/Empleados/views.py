from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    DetailView,
)
# Create your views here.
from django.urls import reverse_lazy

from .models import Empleado


class Inicio(TemplateView):
    template_name = "index.html"


class EmpleadosListView(ListView):
    template_name = "empleados/list-empleados.html"
    #model = Empleado
    paginate_by = 5
    context_object_name = 'ListadoEmpleados'

    def get_queryset(self):
        filtro = self.request.GET.get("nombre",'')
        lista = Empleado.objects.filter(
            first_name__icontains = filtro
        ).order_by('first_name')
        return lista


class EmpleadosbyDepartamentosListView(ListView):
    template_name = "empleados/empleados-by-departamentos.html"
    context_object_name = 'EmpleadosxDepartamento'

    def get_queryset(self):
        filtro = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__short_name = filtro
        ).order_by('first_name')
        return lista

    def get_context_data(self, **kwargs):
        context = super(EmpleadosbyDepartamentosListView, self).get_context_data(**kwargs)
        context['ndepartamento'] = self.kwargs['shorname']
        return context


class AdminEmpleadosListView(ListView):
    template_name = "empleados/admin_empleados.html"
    model = Empleado
    context_object_name = 'Data'
    ordering = ('first_name')
    paginate_by = 10


class EmpleadosUpdateView(UpdateView):
    template_name = "empleados/update-empleado.html"
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('empleados_app:listar_empleados')


class EmpleadoDeleteView(DeleteView):
    template_name = "empleados/delete-empleado.html"
    model = Empleado
    context_object_name = 'Data'
    success_url = reverse_lazy('empleados_app:listar_empleados')


class EmpleadoCreateView(CreateView):
    template_name = "empleados/add-empleado.html"
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('empleados_app:listar_empleados')


class EmpleadoDetailView(DetailView):
    template_name = "empleados/detail-empleado.html"
    model = Empleado
    context_object_name = 'DatosEmpleado'
