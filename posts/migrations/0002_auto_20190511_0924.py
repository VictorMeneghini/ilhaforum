# Generated by Django 2.2.1 on 2019-05-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(blank=True, choices=[(1, 'Ruim'), (2, 'Regular'), (3, 'Bom'), (4, 'Muito Bom'), (5, 'Ótimo')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
