# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0003_forum_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
