# Generated by Django 4.1.6 on 2023-04-11 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0036_alter_session_class_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='Class_teacher',
            field=models.ForeignKey(limit_choices_to={'type': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login'),
        ),
    ]
