# Generated by Django 4.1.6 on 2023-03-08 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_teacher_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_assignment',
            old_name='Subject_name',
            new_name='Subject',
        ),
        migrations.RenameField(
            model_name='tbl_assignment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.DeleteModel(
            name='teacher_detail',
        ),
    ]
