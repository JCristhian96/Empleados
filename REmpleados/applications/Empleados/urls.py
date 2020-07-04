from django.urls import path, re_path, include
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('', 
    views.Inicio.as_view(),
    name='inicio'
),
    path('empleados-all/', 
    views.EmpleadosListView.as_view(),
    name='listar_empleados'
),
    path('list-by-area/<shorname>/',
    views.EmpleadosbyDepartamentosListView.as_view(),
    name='listar-por-area'
),
    path('admin-empleados/',
    views.AdminEmpleadosListView.as_view(),
    name='administrar-empleados'
),
    path('update-empleado/<pk>/',
    views.EmpleadosUpdateView.as_view(),
    name='modificar-empleado'
),
    path('delete-empleado/<pk>/',
    views.EmpleadoDeleteView.as_view(),
    name='eliminar-empleado'
),
    path('add-empleado/',
    views.EmpleadoCreateView.as_view(),
    name='nuevo-empleado'
),
    path('detail-empleado/<pk>/',
    views.EmpleadoDetailView.as_view(),
    name='ver-empleado'
),
]
