# Generated by Django 4.1.6 on 2023-03-09 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0017_alter_tbl_create_class_plus_one'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_create_class',
            old_name='teacher',
            new_name='fname',
        ),
    ]
