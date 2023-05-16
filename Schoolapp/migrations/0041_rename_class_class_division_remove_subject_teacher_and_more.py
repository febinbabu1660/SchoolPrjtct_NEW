# Generated by Django 4.1.6 on 2023-05-08 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0040_class_teachersubject_remove_tbl_batch_course_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Class_division',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='teacher_detail',
            name='email',
            field=models.ForeignKey(limit_choices_to={'type': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(limit_choices_to={'type': 'Teacher'}, to='Schoolapp.tbl_login'),
        ),
    ]
