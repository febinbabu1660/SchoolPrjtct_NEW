# Generated by Django 4.1.6 on 2023-02-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0003_remove_tbl_login_s_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_login',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_login',
            name='fname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tbl_login',
            name='lname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tbl_login',
            name='year_of_join',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_login',
            name='email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tbl_login',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_login',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
