# Generated by Django 2.2 on 2023-02-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0092_auto_20230222_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notification_message', to='api.Messages'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='subscribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notification_subscribe', to='api.UserSubscription'),
        ),
    ]
