from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('platillos',views.platillos, name='platillos'),
    path('platillos/crear', views.crear, name='crear'),
    path('platillos/editar', views.editar, name='editar'),
]