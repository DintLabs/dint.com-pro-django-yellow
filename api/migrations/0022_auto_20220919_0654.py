# Generated by Django 2.2 on 2022-09-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20220914_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpage',
            name='page_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='page_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
