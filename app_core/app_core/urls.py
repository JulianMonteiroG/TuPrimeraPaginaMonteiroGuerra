"""
URL configuration for app_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("index.urls")),

    #app_productos_CRUD
    path('', include(("app_productos.urls","app_productos"), namespace="app_productos")),
    #app_usuarios_CRUD
    path('', include(("app_usuarios.urls","app_usuarios"), namespace="app_usuarios")),
]
