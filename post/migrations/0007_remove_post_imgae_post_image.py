# Generated by Django 4.2 on 2023-10-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_imgae'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imgae',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image'),
        ),
    ]
