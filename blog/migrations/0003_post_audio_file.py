# Generated by Django 5.1.1 on 2024-12-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='blog/audio/'),
        ),
    ]
