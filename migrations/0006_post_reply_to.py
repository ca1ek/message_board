# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reply_to',
            field=models.ForeignKey(null=True, blank=True, to='message_board.Post'),
        ),
    ]
