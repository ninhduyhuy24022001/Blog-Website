# Generated by Django 4.2 on 2023-10-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_proflie_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
