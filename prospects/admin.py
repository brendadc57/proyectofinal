from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Prospect

@admin.register(Prospect)
class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'estatus')
    search_fields = ('nombre', 'correo')
    list_filter = ('estatus',)
