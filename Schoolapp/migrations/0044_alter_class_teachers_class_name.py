# Generated by Django 4.1.6 on 2023-05-08 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0043_remove_subject_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_teachers',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.class_division'),
        ),
    ]
