# Generated by Django 3.2.5 on 2021-08-14 05:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 14, 5, 36, 9, 621419, tzinfo=utc))),
                ('body', models.TextField()),
            ],
        ),
    ]
