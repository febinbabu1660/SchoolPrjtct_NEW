# Generated by Django 4.1.6 on 2023-03-08 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0014_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.teacher_detail'),
        ),
    ]
