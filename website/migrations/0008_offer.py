# Generated by Django 4.1.5 on 2023-01-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_is_closed_service_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('offer_image', models.ImageField(help_text='1920x801 px image for fit background', upload_to='offers')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
