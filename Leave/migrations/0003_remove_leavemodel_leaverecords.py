# Generated by Django 4.1.6 on 2023-03-01 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0002_alter_leavemodel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavemodel',
            name='leaveRecords',
        ),
    ]