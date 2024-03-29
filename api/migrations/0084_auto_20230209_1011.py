# Generated by Django 2.2 on 2023-02-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_auto_20230208_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='verify_email_token',
            new_name='email_token',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='verify_email_token',
            new_name='email_token',
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='email_token_valid',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_token_valid',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
