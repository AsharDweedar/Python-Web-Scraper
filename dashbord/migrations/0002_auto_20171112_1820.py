# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashbord',
            old_name='scrap',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='dashbord',
            old_name='url',
            new_name='title',
        ),
        migrations.AddField(
            model_name='dashbord',
            name='images',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
