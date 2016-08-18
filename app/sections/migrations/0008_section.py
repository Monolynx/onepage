# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('sections', '0007_auto_20160517_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('content', models.TextField(null=True, blank=True)),
                ('show_on_menu', models.BooleanField(default=True, verbose_name='Show on menu')),
                ('show_title_on_section', models.BooleanField(default=True, verbose_name='Show title on section')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Sections',
                'verbose_name': 'Section',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
