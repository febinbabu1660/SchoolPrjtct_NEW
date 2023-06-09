# Generated by Django 4.1.6 on 2023-05-13 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0045_exam_type'),
        ('Teacher', '0028_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.CharField(blank=True, max_length=100, null=True)),
                ('upload_date', models.DateField()),
                ('c_materials', models.FileField(null=True, upload_to='Course_Materials/subject')),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.course')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.subject')),
            ],
        ),
    ]
