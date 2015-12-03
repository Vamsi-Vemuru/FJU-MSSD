# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0003_auto_20151202_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_details',
            name='course_id',
            field=models.ForeignKey(to='Enroll.Enrollment_Details'),
        ),
    ]
