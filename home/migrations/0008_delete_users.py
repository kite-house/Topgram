# Generated by Django 5.0.3 on 2024-04-17 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_users_new_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
