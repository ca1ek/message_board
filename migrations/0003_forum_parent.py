# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0002_thread_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='parent',
            field=models.ForeignKey(blank=True, to='message_board.Forum', null=True),
        ),
    ]
