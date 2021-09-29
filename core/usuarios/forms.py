from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Contraseña'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=_('Recuérdame'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('Ingresaste una contraseña inválida.'))

        return password


class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_('Nombre de usuario'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['username', 'password', 'remember_me']
        return ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_('Ingresaste un nombre de usuario no válido.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no esta activa.'))

        self.user_cache = user

        return username


class SignInViaEmailForm(SignIn):
    email = forms.EmailField(label=_('Correo electrónico'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email', 'password', 'remember_me']
        return ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('Ha introducido una dirección de correo inválida.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no esta activa.'))

        self.user_cache = user

        return email


class SignInViaEmailOrUsernameForm(SignIn):
    email_or_username = forms.CharField(label=_('Correo electrónico o nombre de usuario'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email_or_username', 'password', 'remember_me']
        return ['email_or_username', 'password']

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('Ingresaste una dirección de correo electrónico o un nombre de usuario no válido.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no esta activa.'))

        self.user_cache = user

        return email_or_username


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label=_('Correo electrónico'), help_text=_('Requerido. Ingrese una dirección de correo electrónico existente.'))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('No puedes usar esta dirección de correo electrónico.'))
        return email


class ResendActivationCodeForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_('Correo electrónico o nombre de usuario'))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('Ingresaste una dirección de correo electrónico o un nombre de usuario no válido.'))

        if user.is_active:
            raise ValidationError(_('Esta cuenta ya ha sido activada.'))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_('No se encontró el código de activación.'))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(_('Ya se envió el código de activación. Puedes solicitar un nuevo código en 24 horas.'))

        self.user_cache = user

        return email_or_username


class ResendActivationCodeViaEmailForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Correo electrónico'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('Ha introducido una dirección de correo inválida.'))

        if user.is_active:
            raise ValidationError(_('Esta cuenta ya ha sido activada.'))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_('Código de activación no encontrado.'))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(_('El código de activación ya ha sido enviado.Puede solicitar un nuevo código en 24 horas..'))

        self.user_cache = user

        return email


class RestorePasswordForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Correo electrónico'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('Ha introducido una dirección de correo inválida.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no está activa.'))

        self.user_cache = user

        return email


class RestorePasswordViaEmailOrUsernameForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_('Correo electrónico o nombre de usuario'))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('Ingresó una dirección de correo electrónico o nombre de usuario no válida.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no está activa.'))

        self.user_cache = user

        return email_or_username


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_('Nombre'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Apellido'), max_length=150, required=False)


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label=_('Correo electrónico'))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if email == self.user.email:
            raise ValidationError(_('Por favor ingrese otro correo electrónico.'))

        user = User.objects.filter(Q(email__iexact=email) & ~Q(id=self.user.id)).exists()
        if user:
            raise ValidationError(_('No puedes usar este correo..'))

        return email


class RemindUsernameForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Correo electrónico'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('Ha introducido una dirección de correo inválida.'))

        if not user.is_active:
            raise ValidationError(_('Esta cuenta no está activa.'))

        self.user_cache = user

        return email
