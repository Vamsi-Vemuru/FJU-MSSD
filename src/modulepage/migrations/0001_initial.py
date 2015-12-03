# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title_text', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('specialization', models.CharField(max_length=200, blank=True)),
                ('duration', models.IntegerField(default=0)),
                ('level', models.CharField(default=b'Easy', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=None, blank=True)),
                ('category', models.CharField(max_length=200, blank=True)),
                ('working_format', models.CharField(max_length=200, blank=True)),
                ('hours', models.IntegerField(blank=True)),
                ('course_id', models.ForeignKey(to='modulepage.Course')),
            ],
        ),
        migrations.CreateModel(
            name='FJUUser',
            fields=[
                ('email', models.EmailField(max_length=200, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('display_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('confirm_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Module_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_no', models.IntegerField()),
                ('module_title', models.CharField(max_length=200)),
                ('objective', models.CharField(max_length=500)),
                ('challenge', models.CharField(max_length=200, blank=True)),
                ('show_how', models.CharField(max_length=500, blank=True)),
                ('references', models.CharField(max_length=500, blank=True)),
                ('course_id', models.ForeignKey(to='modulepage.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Module_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('due_date', models.DateField(default=None, blank=True)),
                ('course_id', models.ForeignKey(to='modulepage.Enrollment_Details')),
                ('module_no', models.ForeignKey(to='modulepage.Module_content')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reward', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitTime', models.DateTimeField(auto_now=True)),
                ('username', models.EmailField(max_length=254)),
                ('module_no', models.IntegerField()),
                ('submission', models.FileField(upload_to=b'')),
                ('version', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='reward',
            name='username',
            field=models.ForeignKey(to='modulepage.Submissions'),
        ),
        migrations.AddField(
            model_name='enrollment_details',
            name='email',
            field=models.ForeignKey(to='modulepage.FJUUser'),
        ),
    ]
