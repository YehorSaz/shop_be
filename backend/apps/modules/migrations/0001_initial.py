# Generated by Django 4.2.3 on 2023-07-25 15:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,20}$', 'Only letters min 2 max 20 ch')])),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='ModulePreviewVideosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preview', to='modules.modulemodel')),
            ],
            options={
                'db_table': 'module_preview_videos',
            },
        ),
    ]
