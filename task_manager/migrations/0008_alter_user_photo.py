# Generated by Django 4.0 on 2022-07-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0007_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
