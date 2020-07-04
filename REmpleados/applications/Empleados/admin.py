from django.contrib import admin
from .models import Habilidades, Empleado
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo',
        'first_name',
        'last_name',
        'job',
        'departamento',
    )
    def nombre_completo(self, obj):
        return obj.first_name + " " + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job',)
    ordering = ['first_name',]
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)


class HabilidadesAdmin(admin.ModelAdmin):
    list_display = (
        'habilidades',
        'id',
    )
    search_fields = ('habilidades',)
    ordering = ['habilidades',]

admin.site.register(Habilidades, HabilidadesAdmin)