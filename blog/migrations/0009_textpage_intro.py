# Generated by Django 2.2.6 on 2019-10-31 10:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_textpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpage',
            name='intro',
            field=models.CharField(default=datetime.datetime(2019, 10, 31, 10, 56, 1, 73710, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
