# Generated by Django 4.1.6 on 2023-05-08 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0041_rename_class_class_division_remove_subject_teacher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_teachers',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.course')),
                ('class_teacher', models.ForeignKey(limit_choices_to={'type': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.course')),
            ],
        ),
        migrations.RemoveField(
            model_name='class_division',
            name='class_teacher',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='class_division',
            name='Course_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.course'),
        ),
        migrations.DeleteModel(
            name='TeacherSubject',
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.subject'),
        ),
        migrations.AddField(
            model_name='teacher_subject',
            name='teacher',
            field=models.ManyToManyField(limit_choices_to={'type': 'Teacher'}, to='Schoolapp.tbl_login'),
        ),
    ]