# Generated by Django 2.2 on 2023-02-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_auto_20230202_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='connections',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='connections',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
