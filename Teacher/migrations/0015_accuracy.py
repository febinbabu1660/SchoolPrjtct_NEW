# Generated by Django 4.1.6 on 2023-03-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0014_pass_mark_assignment_marks_pass_mark_attendance_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='accuracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy_value', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
