# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0004_auto_20160517_2139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PortfolioCategories',
            new_name='PortfolioCategory',
        ),
    ]
