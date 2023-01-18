# Generated by Django 4.1.5 on 2023-01-17 23:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_rename_craeted_date_job_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cover_letter',
            field=models.FileField(null=True, upload_to='cober-letter/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(help_text='Kindly note only docx and pdf format are allowed', upload_to='resumes/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])]),
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 23, 55, 48, 880888), help_text='By default its set after 30 days but this can be changed'),
        ),
    ]
