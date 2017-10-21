# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=244, verbose_name='\u7528\u6237')),
                ('audit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('action', models.CharField(max_length=20, verbose_name='\u52a8\u4f5c')),
                ('action_ip', models.CharField(max_length=15, verbose_name='\u7528\u6237IP')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
            ],
            options={
                'ordering': ['-audit_time'],
                'verbose_name_plural': '\u5ba1\u8ba1\u4fe1\u606f\u7ba1\u7406',
                'default_permissions': (),
                'verbose_name': '\u5ba1\u8ba1\u4fe1\u606f',
                'permissions': (('view_message', '\u67e5\u770b\u64cd\u4f5c\u8bb0\u5f55'), ('edit_message', '\u7ba1\u7406\u64cd\u4f5c\u8bb0\u5f55')),
            },
        ),
        migrations.CreateModel(
            name='UserCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='\u547d\u4ee4\u522b\u540d')),
                ('command', models.TextField(blank=True, verbose_name='\u7cfb\u7edf\u547d\u4ee4')),
                ('is_allow', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u8fdc\u7a0b\u547d\u4ee4',
                'verbose_name_plural': '\u8fdc\u7a0b\u547d\u4ee4\u7ba1\u7406',
                'permissions': (('edit_remote_permission', '\u7ba1\u7406\u8fdc\u7a0b\u6743\u9650'),),
            },
        ),
        migrations.CreateModel(
            name='UserDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='\u76ee\u5f55\u522b\u540d')),
                ('directory', models.TextField(blank=True, verbose_name='\u7cfb\u7edf\u76ee\u5f55')),
                ('is_allow', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u8fdc\u7a0b\u76ee\u5f55',
                'verbose_name_plural': '\u8fdc\u7a0b\u76ee\u5f55\u7ba1\u7406',
            },
        ),
    ]
