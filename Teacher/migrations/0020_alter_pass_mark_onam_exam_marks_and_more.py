# Generated by Django 4.1.6 on 2023-04-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0019_alter_pass_mark_onam_exam_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass_mark',
            name='onam_exam_marks',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pass_mark',
            name='xmas_exam_marks',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]