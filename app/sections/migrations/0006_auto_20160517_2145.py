# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0005_auto_20160517_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='title',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='content',
            field=models.TextField(verbose_name='Content', default='asd'),
            preserve_default=False,
        ),
    ]
