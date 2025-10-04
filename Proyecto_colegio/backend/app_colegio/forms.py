from django import forms


class Register(forms.Form):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="email")
    username = forms.CharField(label="username")
    password = forms.CharField(
        label="contraseña",
        widget= forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget= forms.PasswordInput()
    )


class AuthLogin(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(
        label="contraseña",
        widget= forms.PasswordInput()
    )

