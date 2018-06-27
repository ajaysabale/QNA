# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='op1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='op2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='op3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='op4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='question',
            field=models.ForeignKey(default=0, to='port.Question'),
        ),
    ]
