# Generated by Django 4.2.7 on 2024-02-16 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_coursemodel_table'),
        ('groups', '0007_alter_groupmodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='courses.coursemodel'),
        ),
    ]
