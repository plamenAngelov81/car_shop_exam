# Generated by Django 4.2.2 on 2023-06-15 11:44

import car_shop_exam.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[car_shop_exam.web.models.min_char_check], verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)], verbose_name='Age')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]
