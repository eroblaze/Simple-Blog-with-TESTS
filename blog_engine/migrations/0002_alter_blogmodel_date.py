# Generated by Django 3.2.5 on 2021-08-14 05:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 14, 5, 37, 39, 426642, tzinfo=utc)),
        ),
    ]
