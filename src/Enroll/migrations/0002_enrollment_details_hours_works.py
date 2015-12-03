# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment_details',
            name='hours_works',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
