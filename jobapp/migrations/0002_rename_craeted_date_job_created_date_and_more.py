# Generated by Django 4.1.5 on 2023-01-17 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='craeted_date',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 23, 52, 29, 413948)),
        ),
    ]
