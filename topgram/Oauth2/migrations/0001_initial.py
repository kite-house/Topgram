# Generated by Django 5.0.3 on 2024-04-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('display_name', models.CharField(default='', max_length=150)),
                ('avatar', models.CharField(default='https://avatars.mds.yandex.net/i?id=d44d7c579e55f0bdfad006c09502bcb7168a8444-10889692-images-thumbs&n=13', max_length=1000)),
                ('chat_list', models.JSONField(default=list)),
                ('messages', models.JSONField(default=dict)),
                ('last_online', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]