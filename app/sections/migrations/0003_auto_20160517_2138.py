# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20160517_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategories',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=63, verbose_name='Title')),
            ],
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='categories',
            field=models.ForeignKey(verbose_name='Categories', default=1, to='sections.PortfolioCategories'),
            preserve_default=False,
        ),
    ]
