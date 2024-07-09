# Generated by Django 5.0.6 on 2024-07-08 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='post/images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.post')),
            ],
        ),
    ]
