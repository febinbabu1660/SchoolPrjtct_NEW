# Generated by Django 4.1.6 on 2023-03-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0013_remove_mark_date_remove_mark_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass_mark',
            name='assignment_marks',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='pass_mark',
            name='attendance_mark',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
