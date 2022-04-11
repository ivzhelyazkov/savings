from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

from savings.common.validators import validate_only_letters
from colorfield.fields import ColorField

CATEGORY_NAME_MAX_LENGTH = 30
CATEGORY_NAME_MIN_LENGTH = 2


class IncomingCategory(models.Model):
    name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(CATEGORY_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    color = ColorField()

    def __str__(self):
        return f'{self.name}'


class Incoming(models.Model):
    amount = models.FloatField(
        validators=(
            MinValueValidator(0.01),
        ),
    )

    date = models.DateField(
        default=now
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        IncomingCategory,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def get_my_model_name(self):
        return self._meta.model_name

    def __str__(self):
        return f'{self.amount} by {self.user} on {self.date}'


class ExpenseCategory(models.Model):
    name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LENGTH,
        unique=True,
        validators=(
            MinLengthValidator(CATEGORY_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    color = ColorField()

    def __str__(self):
        return f'{self.name}'


class Expense(models.Model):
    ORDINARY = "Ordinary"
    EXTRAORDINARY = "Extraordinary"
    TYPES = [(x, x) for x in (ORDINARY, EXTRAORDINARY,)]

    amount = models.FloatField(
        validators=(
            MinValueValidator(0.01),
        ),
    )

    date = models.DateField(
        default=now
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def get_my_model_name(self):
        return self._meta.model_name

    def __str__(self):
        return f'{self.amount} by {self.user} on {self.date}'


# class AboutContent(models.Model):
#     AUTHOR_MAX_LEN = 25
#
#     author = models.CharField(
#         default='Super',
#         max_length=AUTHOR_MAX_LEN,
#     )
#
#     paragraph_1 = models.TextField()
#
#     paragraph_2 = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     paragraph_3 = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     paragraph_4 = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     paragraph_5 = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     # optional ImageFields to be added later\
#
#     def __str__(self):
#         return f'About Content by {self.author}'