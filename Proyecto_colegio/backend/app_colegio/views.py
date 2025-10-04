from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import Register, AuthLogin

def home_view(request):
    return render(request, 'home.html')


# Vista para registro usando User
def register_view(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                messages.error(request, "Las contraseñas no coinciden")
                return render(request, 'registro.html', {'form': form})

            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe")
                return render(request, 'registro.html', {'form': form})

            # Crear el usuario
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = Register()
    return render(request, 'registro.html', {'form': form})


# Vista para login usando User
def login_view(request):
    if request.method == 'POST':
        form = AuthLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Has iniciado sesión como {username}")
                return redirect('inicio')  # Redirige a home
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = AuthLogin()
    return render(request, 'login.html', {'form': form})


# Vista para logout
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('login')
