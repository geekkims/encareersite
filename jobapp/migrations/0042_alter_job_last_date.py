# Generated by Django 4.1.5 on 2023-01-22 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0041_alter_job_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 21, 22, 14, 34, 491308), help_text='By default its set after 30 days but this can be changed'),
        ),
    ]
