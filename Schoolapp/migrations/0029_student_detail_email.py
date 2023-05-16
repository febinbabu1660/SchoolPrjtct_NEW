# Generated by Django 4.1.6 on 2023-04-01 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0028_student_detail_alter_course_teacher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detail',
            name='email',
            field=models.ForeignKey(limit_choices_to={'email__type': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login'),
        ),
    ]