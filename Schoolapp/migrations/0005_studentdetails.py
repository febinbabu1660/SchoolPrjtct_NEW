# Generated by Django 4.1.6 on 2023-02-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0004_tbl_login_department_tbl_login_fname_tbl_login_lname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=100, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('hname', models.CharField(blank=True, max_length=100, null=True)),
                ('father', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('pmobile', models.CharField(default=0, max_length=200)),
                ('email', models.EmailField(blank=True, default=0, max_length=254, null=True)),
                ('dob', models.DateField()),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('pschool', models.CharField(blank=True, max_length=100, null=True)),
                ('mark', models.CharField(blank=True, max_length=200, null=True)),
                ('Stream', models.CharField(blank=True, max_length=100, null=True)),
                ('slanguage', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('gname', models.CharField(blank=True, max_length=100, null=True)),
                ('gmobile', models.CharField(blank=True, max_length=200, null=True)),
                ('gemail', models.EmailField(blank=True, default=0, max_length=254, null=True)),
                ('gpassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
