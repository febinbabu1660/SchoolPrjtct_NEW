# Generated by Django 4.1.6 on 2023-03-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0003_rename_subject_name_tbl_assignment_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_assignment',
            name='submission_date',
            field=models.DateField(),
        ),
    ]
