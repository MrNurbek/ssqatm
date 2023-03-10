# Generated by Django 4.1.6 on 2023-02-02 07:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dastur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dasturnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('servernomi', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('pudratchi', models.TextField(blank=True, max_length=500, null=True)),
                ('ishgatushgandavt', models.TextField(blank=True, max_length=500, null=True)),
                ('tolovharajatlari', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500)),
                ('tell', models.TextField(blank=True, max_length=500)),
                ('login', models.TextField(blank=True, max_length=500, null=True)),
                ('parol', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('holati', models.TextField(blank=True, max_length=500, null=True)),
                ('rusumi', models.TextField(blank=True, max_length=500, null=True)),
                ('xolat', models.TextField(blank=True, max_length=500, null=True)),
                ('foydalanishgatopshirilganvaqt', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500, null=True)),
                ('tel', models.TextField(blank=True, max_length=500, null=True)),
                ('pudratchi', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('lavozim', models.TextField(blank=True, max_length=500, null=True)),
                ('vazifasi', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
                ('pasportraqam', models.TextField(blank=True, max_length=500, null=True)),
                ('jshir', models.TextField(blank=True, max_length=500, null=True)),
                ('manzil', models.TextField(blank=True, max_length=500, null=True)),
                ('oilaviyholat', models.TextField(blank=True, max_length=500, null=True)),
                ('malumoti', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Internet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinetlogin', models.TextField(blank=True, max_length=500, null=True)),
                ('cabinetparol', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('pudratchi', models.TextField(blank=True, max_length=500, null=True)),
                ('ishgatushgandavt', models.TextField(blank=True, max_length=500, null=True)),
                ('tolovharajatlari', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('holati', models.TextField(blank=True, max_length=500, null=True)),
                ('rusumi', models.TextField(blank=True, max_length=500, null=True)),
                ('xolat', models.TextField(blank=True, max_length=500, null=True)),
                ('foydalanishgatopshirilganvaqt', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500, null=True)),
                ('tel', models.TextField(blank=True, max_length=500, null=True)),
                ('pudratchi', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kompyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raqam', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('monitor', models.TextField(blank=True, max_length=500, null=True)),
                ('protsesor', models.TextField(blank=True, max_length=500, null=True)),
                ('matplata', models.TextField(blank=True, max_length=500, null=True)),
                ('opiratevka', models.TextField(blank=True, max_length=500, null=True)),
                ('videokarta', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
                ('xolat', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raqam', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('monitor', models.TextField(blank=True, max_length=500, null=True)),
                ('protsesor', models.TextField(blank=True, max_length=500, null=True)),
                ('matplata', models.TextField(blank=True, max_length=500, null=True)),
                ('opiratevka', models.TextField(blank=True, max_length=500, null=True)),
                ('videokarta', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
                ('xolat', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taklif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=500, null=True)),
                ('taklifsohasi', models.TextField(blank=True, max_length=500, null=True)),
                ('tuliqtavsifi', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wifi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminlogin', models.TextField(blank=True, max_length=500, null=True)),
                ('adminparol', models.TextField(blank=True, max_length=500, null=True)),
                ('tashkilotnomi', models.TextField(blank=True, max_length=500, null=True)),
                ('qurulmarusumi', models.TextField(blank=True, max_length=500, null=True)),
                ('xolati', models.TextField(blank=True, max_length=500, null=True)),
                ('foydalanishgatopshirilganvaqti', models.TextField(blank=True, max_length=500, null=True)),
                ('masul', models.TextField(blank=True, max_length=500, null=True)),
                ('tell', models.TextField(blank=True, max_length=500, null=True)),
                ('wifinomi', models.TextField(blank=True, max_length=500, null=True)),
                ('parol', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('parol', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
