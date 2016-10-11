# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0012_auto_20160924_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionitem',
            name='template',
            field=models.CharField(max_length=1023, choices=[('widgets/service_item.html', 'Service Item'), ('widgets/slider_item.html', 'Slider Item'), ('widgets/team_item.html', 'Team Item')]),
        ),
    ]
