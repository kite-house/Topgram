# Generated by Django 5.0.3 on 2024-04-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_users_new_avatar_alter_users_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='new_avatar',
        ),
    ]
