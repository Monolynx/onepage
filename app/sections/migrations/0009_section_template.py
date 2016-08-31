# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0008_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='template',
            field=models.CharField(null=True, max_length=1023, choices=[('no elo', 'one'), ('no tak', 'two'), ('piotrek', 'three')], blank=True),
        ),
    ]
