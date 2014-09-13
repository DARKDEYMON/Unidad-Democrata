# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20140910_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nivel_2',
            options={'verbose_name': 'Nivel 2', 'verbose_name_plural': 'Nivel 2'},
        ),
        migrations.AddField(
            model_name='nivel_2',
            name='sircunscripcion',
            field=models.CharField(default='ninguno', max_length=100),
            preserve_default=False,
        ),
    ]
