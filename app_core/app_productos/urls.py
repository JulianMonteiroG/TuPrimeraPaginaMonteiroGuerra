from django.urls import path
from .views import listar_productos , create_productos , update_productos , delete_productos

app_name = "app_productos"

urlpatterns = [
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('crear_productos/', create_productos, name="create_productos"),
    path('actualizar_productos/<int:pk>/', update_productos, name="update_productos"),
    path('eliminar_productos/<int:pk>/', delete_productos, name="delete_productos"),
]