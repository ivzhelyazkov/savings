from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from savings.accounts.managers import SavingsUserManager

from savings.common.validators import validate_only_letters


# custom app user modifying the built-in model - only username, password, date, staff
class SavingsUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = SavingsUserManager()


# app profile model adding fields that are not required for login
class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    budget = models.FloatField(
        validators=(
            MinValueValidator(0.01),
        ),
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        SavingsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
