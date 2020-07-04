from django.urls import path, re_path, include
from . import views

app_name = 'departamentos_app'

urlpatterns = [
    path('list-departamentos/',
    views.DepartamentosListView.as_view(),
    name='listar-departamentos'
),
    path('new-departamento/',
    views.NewDepartamentoForm.as_view(),
    name='nuevo-departamento'
),
]