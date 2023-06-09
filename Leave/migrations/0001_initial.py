# Generated by Django 4.1.6 on 2023-02-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leaveModel',
            fields=[
                ('leaveId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=30)),
                ('leaveDate', models.DateField()),
                ('leaveDiv', models.CharField(max_length=10)),
                ('leaveReason', models.CharField(max_length=50)),
                ('leaveStatus', models.BooleanField(default=False, verbose_name='Approved')),
                ('leaveRecords', models.FileField(upload_to='media/leave/')),
            ],
        ),
    ]
