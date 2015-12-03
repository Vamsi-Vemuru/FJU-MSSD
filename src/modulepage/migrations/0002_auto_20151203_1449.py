# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modulepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='course_id',
            field=models.ForeignKey(default=django.utils.timezone.now, to='modulepage.Course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submissions',
            name='module_no',
            field=models.ForeignKey(to='modulepage.Module_content'),
        ),
    ]
