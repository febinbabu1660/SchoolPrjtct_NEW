# Generated by Django 4.1.6 on 2023-03-13 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0021_alter_teacher_detail_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetail',
            old_name='mark',
            new_name='mark_obtained',
        ),
    ]