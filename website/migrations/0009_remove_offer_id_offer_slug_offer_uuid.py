# Generated by Django 4.1.5 on 2023-01-20 07:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='id',
        ),
        migrations.AddField(
            model_name='offer',
            name='slug',
            field=models.CharField(default='hejdkfdjkfjf', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
