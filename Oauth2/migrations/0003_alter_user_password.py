# Generated by Django 5.0.3 on 2024-04-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oauth2', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
