# Generated by Django 4.0.3 on 2022-03-29 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_expense_date_alter_expense_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.CharField(choices=[('Ordinary', 'Ordinary'), ('Extraordinary', 'Extraordinary')], max_length=13),
        ),
        migrations.AlterField(
            model_name='incoming',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
