# Generated by Django 4.1.6 on 2023-05-10 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0045_exam_type'),
        ('Teacher', '0025_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Assignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('submission_date', models.DateField()),
                ('qpaper', models.FileField(null=True, upload_to='Assignment/subject')),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.course')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.subject')),
            ],
        ),
    ]
