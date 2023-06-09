# Generated by Django 4.1.6 on 2023-04-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0027_delete_studentdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=100, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('hname', models.CharField(blank=True, max_length=100, null=True)),
                ('father', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('pmobile', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField()),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('pschool', models.CharField(blank=True, max_length=100, null=True)),
                ('mark_obtained', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('gname', models.CharField(blank=True, max_length=100, null=True)),
                ('gmobile', models.CharField(blank=True, max_length=200, null=True)),
                ('gemail', models.EmailField(blank=True, default=0, max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_name',
            field=models.ForeignKey(limit_choices_to={'email__type': 'teacher'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login'),
        ),
    ]
