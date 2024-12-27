from django.urls import path 
from .views import UserLoginView , PanelView , UserListView , UserCreateView , UserUpdateView , logout_view

app_name = "app_usuarios"

urlpatterns = [
    path("login/", UserLoginView.as_view() , name="login"),
    path("panel/", PanelView.as_view() , name="panel"),
    path("usuario_list/", UserListView.as_view() , name="usuario_list"),
    path("usuario_create/", UserCreateView.as_view() , name="usuario_create"),
    path("usuario_edit/<int:pk>/", UserUpdateView.as_view() , name="usuario_edit"),
    path('logout/', logout_view, name='logout'),
]