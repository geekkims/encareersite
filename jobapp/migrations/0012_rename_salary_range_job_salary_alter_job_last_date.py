# Generated by Django 4.1.5 on 2023-01-19 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0011_remove_job_salary_job_salary_range_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='salary_range',
            new_name='salary',
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 18, 16, 41, 48, 109786), help_text='By default its set after 30 days but this can be changed'),
        ),
    ]