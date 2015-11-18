# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Forum name', max_length=60)),
                ('description', models.TextField(verbose_name='Description')),
                ('dropdown_open', models.BooleanField(verbose_name='Subforums dropdown open by default', default=False)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('super_admin', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='super_admin')),
                ('viewable_by', models.ForeignKey(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField(verbose_name='Message')),
                ('written_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('topic', models.CharField(verbose_name='Thread topic', max_length=60)),
                ('started_on', models.DateTimeField(auto_now_add=True)),
                ('started_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='message_board.Thread'),
        ),
        migrations.AddField(
            model_name='post',
            name='written_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
