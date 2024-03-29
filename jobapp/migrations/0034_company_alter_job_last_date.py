# Generated by Django 4.1.5 on 2023-01-20 20:23

import datetime
from django.db import migrations, models
import jobapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0033_alter_job_last_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300)),
                ('company_logo', models.ImageField(help_text='1920x801 px image for fit background', null=True, upload_to=jobapp.models.upload_to)),
                ('industry', models.CharField(choices=[('IT', 'Information Technology'), ('FIN', 'Finance'), ('MAN', 'Manufacturing'), ('RET', 'Retail'), ('TRA', 'Transportation'), ('CON', 'Construction'), ('ENE', 'Energy'), ('HEA', 'Healthcare'), ('EDU', 'Education'), ('AGR', 'Agriculture'), ('GOV', 'Government'), ('TEL', 'Telecommunications'), ('ENT', 'Entertainment'), ('SER', 'Service'), ('TOU', 'Tourism'), ('MED', 'Media'), ('FOO', 'Food'), ('FAS', 'Fashion'), ('AUT', 'Automotive'), ('HOU', 'Housing'), ('MIN', 'Mining'), ('PET', 'Petroleum'), ('CHE', 'Chemical'), ('ENE', 'Energy'), ('INS', 'Insurance'), ('PRO', 'Professional Services'), ('COM', 'Communications'), ('LOG', 'Logistics'), ('MAR', 'Marketing'), ('PUB', 'Publishing'), ('TEC', 'Technology'), ('TRA', 'Trade'), ('WHO', 'Wholesale'), ('TRN', 'Transportation')], max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 19, 23, 23, 39, 60510), help_text='By default its set after 30 days but this can be changed'),
        ),
    ]
