# Generated by Django 3.2.5 on 2022-06-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube_url',
            field=models.URLField(null=True),
        ),
    ]
