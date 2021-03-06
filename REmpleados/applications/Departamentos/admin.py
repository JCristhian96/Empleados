from django.contrib import admin
from .models import Departamento

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_name',
        'anulate',
    )
    search_fields = ('name',)
    list_filter = ('anulate',)
    ordering = ['name',]


admin.site.register(Departamento, DepartamentoAdmin)