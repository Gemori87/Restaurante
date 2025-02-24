from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')



def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)  
        if form.is_valid():
            user = form.save()  
            print(f"Usuario {user.username} creado.")  
            login(request, user)  
            messages.success(request, f'Cuenta creada para {user.username}! Bienvenido.')
            return redirect('perfil')  
        else:
            print("Formulario no válido")  
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registration/registrar.html', {'form': form})

def platillos(request):
    return render(request, 'platillos/index.html')
def crear(request):
    return render(request, 'platillos/crear.html')

def editar(request):
    return render(request, 'platillos/editar.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():  
            return redirect('inicio')  
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'registration/perfil.html', {'user': request.user})

def recuperar_contrasena(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            nueva_contrasena = User.objects.make_random_password()
            user.set_password(nueva_contrasena)
            user.save()

            
            send_mail(
                "Recuperación de contraseña",
                f"Hola {user.username}, tu nueva contraseña es: {nueva_contrasena}",
                "tuemail@gmail.com",
                [email],
                fail_silently=False,
            )

            messages.success(request, "Se ha enviado un correo con tu nueva contraseña.")
            return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "No se encontró una cuenta con ese correo.")
    
    return render(request, "recuperar_contrasena.html")

