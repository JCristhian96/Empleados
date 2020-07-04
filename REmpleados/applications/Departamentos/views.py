from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import NewDepartamento
# Create your views here.
from .models import Departamento
from applications.Empleados.models import Empleado

class DepartamentosListView(ListView):
    template_name = "departamentos/list-departamentos.html"
    model = Departamento
    context_object_name = 'ListadoDepartamentos'


class NewDepartamentoForm(FormView):
    template_name = 'departamentos/new-departamento.html'
    form_class = NewDepartamento
    success_url = reverse_lazy('departamentos_app:listar-departamentos')

    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shorname']
        )
        depa.save()
        newempleado = Empleado(
            first_name = form.cleaned_data['nombres'],
            last_name = form.cleaned_data['apellidos'],
            job = '1',
            departamento = depa
        )
        newempleado.save()
        return super(NewDepartamentoForm, self).form_valid(form)