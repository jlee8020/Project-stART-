# Generated by Django 3.0.4 on 2020-03-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile_profilephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='filename',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilephoto',
            name='filename',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]