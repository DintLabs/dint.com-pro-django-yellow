# Generated by Django 2.2 on 2023-02-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0074_auto_20230118_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
