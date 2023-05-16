# Generated by Django 4.1.6 on 2023-03-13 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0022_rename_mark_studentdetail_mark_obtained'),
        ('Teacher', '0005_alter_tbl_assignment_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.studentdetail')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.subject')),
            ],
        ),
    ]