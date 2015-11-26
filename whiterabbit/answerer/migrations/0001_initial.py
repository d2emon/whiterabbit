# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'upload', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
