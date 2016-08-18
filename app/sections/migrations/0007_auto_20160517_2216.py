# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0006_auto_20160517_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfoliocategory',
            options={'verbose_name_plural': 'Portfolio Categories', 'verbose_name': 'Portfolio Category'},
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='title',
            field=models.CharField(default='default', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
