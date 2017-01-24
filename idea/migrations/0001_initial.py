# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_name', models.CharField(max_length=200)),
                ('idea_text', models.TextField()),
                ('idea_rank', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Идеи',
                'db_table': 'idea',
            },
        ),
    ]