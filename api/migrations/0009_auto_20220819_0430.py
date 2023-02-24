# Generated by Django 2.2 on 2022-08-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220818_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmessages',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='banner_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='banner_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
