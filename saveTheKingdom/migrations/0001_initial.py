# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wanderers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="What's your nickname/title?", max_length=20)),
                ('comment', models.TextField(help_text='A quote that resonates with your character', max_length=200)),
                ('status', models.CharField(choices=[('h', 'Hero of Xeek'), ('l', 'Loser of the Land')], default='l', max_length=1)),
            ],
            options={
                'ordering': ['name', 'status', 'comment'],
            },
        ),
    ]
