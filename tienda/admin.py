from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  #Solo ver, No modificar

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  #Solo ver, No modificar

admin.site.register(CategoriaProd, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
