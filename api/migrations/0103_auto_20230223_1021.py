# Generated by Django 2.2 on 2023-02-23 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0102_auto_20230222_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstories',
            name='is_archived',
            field=models.BooleanField(default=False),
        )
    ]
