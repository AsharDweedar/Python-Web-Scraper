# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0002_auto_20171112_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashbord',
            name='images',
        ),
        migrations.AddField(
            model_name='dashbord',
            name='url',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
