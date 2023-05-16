# Generated by Django 4.1.6 on 2023-03-30 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0026_alter_course_teacher_name'),
        ('Teacher', '0016_remove_accuracy_accuracy_value_accuracy_mse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass_mark',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pass_mark',
            name='email',
            field=models.ForeignKey(default='sachin@gmail.com', limit_choices_to={'type': 'student'}, on_delete=django.db.models.deletion.CASCADE, to='Schoolapp.tbl_login'),
        ),
        migrations.DeleteModel(
            name='accuracy',
        ),
    ]