# Generated by Django 2.2 on 2022-11-24 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_userbookmarks_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCloseFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('close_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='close_friend', to=settings.AUTH_USER_MODEL)),
                ('main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
