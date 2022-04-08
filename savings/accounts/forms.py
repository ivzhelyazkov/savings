from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.validators import MinLengthValidator

from savings.accounts.models import Profile
from savings.common.helpers import BootstrapFormMixin
from savings.common.validators import validate_only_letters


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    # form validation is done here using the same validators as in the model
    # customized all fields to get better labels, placeholders and hide password help_text
    username = forms.CharField(
        max_length=get_user_model().USERNAME_MAX_LENGTH,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Username...',
            }
        ),
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password...',
            },
        ),
        help_text=None,
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your Password...',
            },
        ),
        help_text=None,
    )

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your First Name...',
            },
        ),
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Last Name...',
            },
        ),
    )

    budget = forms.FloatField(
        label='Budget',
        widget=forms.TextInput(
            attrs=
            {'class': 'form-control',
             'placeholder': 'Your Starting Budget...',
             },
        ),
    )

    email = forms.EmailField(
        required=False,
        label='Email (Optional)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address...',
            },
        ),
    )

    # used to call the bootstrapmixin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    # used to create a profile object
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            budget=self.cleaned_data['budget'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'budget', 'email')
