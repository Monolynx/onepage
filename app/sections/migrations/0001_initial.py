# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, auto_created=True, to='cms.CMSPlugin', parent_link=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=31)),
                ('content', models.CharField(verbose_name='Content', max_length=1023)),
                ('image', filer.fields.image.FilerImageField(null=True, to='filer.Image')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
