# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('cms', '0014_auto_20160404_1908'),
        ('sections', '0011_auto_20160909_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=31)),
                ('content', models.CharField(verbose_name='Content', max_length=1023)),
                ('template', models.CharField(blank=True, choices=[('widgets/service_item.html', 'Service Item'), ('widgets/slider_item.html', 'Slider Item'), ('widgets/team_item.html', 'Team Item')], null=True, max_length=1023)),
                ('image', filer.fields.image.FilerImageField(default='', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Section Items',
                'verbose_name': 'Section Item (title, content, image)',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='service',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image',
        ),
        migrations.AlterField(
            model_name='section',
            name='template',
            field=models.CharField(blank=True, choices=[('widgets/service.html', 'Service'), ('widgets/slider.html', 'Slider'), ('widgets/portfolio.html', 'Portfolio'), ('widgets/team.html', 'Team')], null=True, max_length=1023),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
