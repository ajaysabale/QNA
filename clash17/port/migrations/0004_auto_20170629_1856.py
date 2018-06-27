# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_users_q_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(default=0, to='port.Users'),
        ),
    ]
