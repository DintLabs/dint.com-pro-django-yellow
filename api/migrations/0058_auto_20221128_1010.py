# Generated by Django 2.2 on 2022-11-28 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_userclosefriends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
