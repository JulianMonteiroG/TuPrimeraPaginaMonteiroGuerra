from django.urls import path 
from .views import listar_usuarios , create_usuarios , delete_usuarios 

app_name = "app_usuarios"

urlpatterns = [
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("crear_usuarios/", create_usuarios, name="create_usuarios"),
    path("eliminar_usuarios/<int:pk>/", delete_usuarios, name="delete_usuarios"),
]