# Generated by Django 4.1.6 on 2023-02-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_studentlogin',
            fields=[
                ('s_id', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
