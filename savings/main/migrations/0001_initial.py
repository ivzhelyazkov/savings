# Generated by Django 4.0.3 on 2022-04-11 15:02

import colorfield.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import savings.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), savings.common.validators.validate_only_letters])),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='IncomingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), savings.common.validators.validate_only_letters])),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.incomingcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('Ordinary', 'Ordinary'), ('Extraordinary', 'Extraordinary')], max_length=13)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.expensecategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
