# Generated by Django 4.2.3 on 2023-07-28 14:57

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.RegexValidator('^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=(?:.*[`~!@#$%^&*()\\-_+=\\\\\\|\\\'\\"\\;\\:\\/?.>,<\\[\\]\\{\\}]))[a-zA-Z\\d`~!@#$%^&*()\\-_+=\\\\\\|\\\'\\"\\;\\:\\/?.>,<\\[\\]\\{\\}]{8,30}$', ['min 1 lowercase ch', 'min 1 uppercase ch', 'min 1 digit', 'min 1 special character', 'length 8-30'])])),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^(?:(?!.*[эЭыЫ]))[А-яіІїЇґҐєЄ-]{2,50}$', ['Only Ukrainian letters or "-"', 'min 2 characters', 'max 50 characters'])])),
                ('surname', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^(?:(?!.*[эЭыЫ]))[А-яіІїЇґҐєЄ-]{2,50}$', ['Only Ukrainian letters or "-"', 'min 2 characters', 'max 50 characters'])])),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^\\d{12}$', 'Only numbers, 12 numbers')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
