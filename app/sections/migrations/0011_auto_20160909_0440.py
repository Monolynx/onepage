# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('cms', '0014_auto_20160404_1908'),
        ('sections', '0010_auto_20160902_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, to='cms.CMSPlugin', parent_link=True, primary_key=True)),
                ('title', models.CharField(max_length=31, verbose_name='Title')),
                ('content', models.CharField(max_length=1023, verbose_name='Content')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', default='')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='section',
            name='template',
            field=models.CharField(max_length=1023, null=True, choices=[('widgets/slider.html', 'Slider'), ('widgets/service.html', 'Service'), ('widgets/portfolio.html', 'Portfolio')], blank=True),
        ),
    ]
