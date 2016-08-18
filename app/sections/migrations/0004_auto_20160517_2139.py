# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_auto_20160517_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='categories',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='categories',
            field=models.ManyToManyField(verbose_name='Categories', to='sections.PortfolioCategories'),
        ),
    ]
