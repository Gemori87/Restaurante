from django.urls import path
from . import views
from .views import recuperar_contrasena
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registrar/', views.registrar_usuario, name='registration/registrar_usuario'),
    path("recuperar-contrasena/", recuperar_contrasena, name="recuperar_contrasena"),
    path('perfil/', views.perfil, name='perfil'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('platillos',views.platillos, name='platillos'),
    path('platillos/crear', views.crear, name='crear'),
    path('platillos/editar', views.editar, name='editar'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]