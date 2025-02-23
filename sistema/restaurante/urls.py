from django.urls import path
from . import views
from .views import recuperar_contrasena

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path("recuperar-contrasena/", recuperar_contrasena, name="recuperar_contrasena"),
    path('nosotros', views.nosotros, name='nosotros'),
    path('platillos',views.platillos, name='platillos'),
    path('platillos/crear', views.crear, name='crear'),
    path('platillos/editar', views.editar, name='editar'),
]