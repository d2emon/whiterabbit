# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_realization'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='estimate',
            field=models.IntegerField(default=1),
        ),
    ]
