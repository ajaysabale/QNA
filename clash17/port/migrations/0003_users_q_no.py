# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20170628_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='q_no',
            field=models.IntegerField(default=0),
        ),
    ]
