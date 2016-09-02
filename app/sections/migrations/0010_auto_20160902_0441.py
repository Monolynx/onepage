# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0006_auto_20160623_1627'),
        ('sections', '0009_section_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=31)),
                ('content', models.CharField(verbose_name='Content', max_length=1023)),
                ('image', filer.fields.image.FilerImageField(default='', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Sliders',
                'verbose_name': 'Slider',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='image',
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Portfolios', 'verbose_name': 'Portfolio'},
        ),
        migrations.AddField(
            model_name='portfolio',
            name='categories',
            field=models.ManyToManyField(verbose_name='Categories', to='sections.PortfolioCategory'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=filer.fields.image.FilerImageField(default='', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='content',
            field=models.CharField(verbose_name='Content', max_length=1023),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=31),
        ),
        migrations.AlterField(
            model_name='section',
            name='template',
            field=models.CharField(blank=True, null=True, max_length=1023, choices=[('widgets/service.html', 'Service'), ('widgets/portfolio.html', 'Portfolio')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=filer.fields.image.FilerImageField(default='', to='filer.Image'),
        ),
        migrations.DeleteModel(
            name='PortfolioItem',
        ),
    ]
