# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='Portfolio', verbose_name='Title', max_length=255)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField()),
                ('image', filer.fields.image.FilerImageField(to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=filer.fields.image.FilerImageField(to='filer.Image'),
        ),
    ]
