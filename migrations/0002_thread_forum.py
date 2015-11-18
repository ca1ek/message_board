# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(to='message_board.Forum', default=''),
            preserve_default=False,
        ),
    ]
