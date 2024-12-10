from django.contrib import admin
from app_productos.models import Producto
from app_usuarios.models import Usuario


# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)