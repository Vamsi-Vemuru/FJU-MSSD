# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0002_enrollment_details_hours_works'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment_details',
            old_name='hours_works',
            new_name='hours',
        ),
    ]
