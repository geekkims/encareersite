# Generated by Django 4.1.5 on 2023-01-18 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_alter_job_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 17, 20, 59, 45, 971086), help_text='By default its set after 30 days but this can be changed'),
        ),
    ]
