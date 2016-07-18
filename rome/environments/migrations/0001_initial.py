# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('ue4_map_url', models.URLField(blank=True, default='')),
                ('instructors', models.ManyToManyField(related_name='lessons', to='accounts.InstructorProfile')),
                ('students', models.ManyToManyField(related_name='lessons', to='accounts.LearnerProfile')),
            ],
        ),
    ]