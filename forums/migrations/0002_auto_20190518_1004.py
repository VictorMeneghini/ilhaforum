# Generated by Django 2.2.1 on 2019-05-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]