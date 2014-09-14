# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20140913_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='nivel_3',
            name='municio_recinto',
            field=models.CharField(default='ninguno', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='control_electoral',
            name='sircunscripcion',
            field=models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34'), (b'C35', b'C35'), (b'C36', b'C36'), (b'C37', b'C37'), (b'C38', b'C38'), (b'C39', b'C39')]),
        ),
        migrations.AlterField(
            model_name='nivel_2',
            name='sircunscripcion',
            field=models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34'), (b'C35', b'C35'), (b'C36', b'C36'), (b'C37', b'C37'), (b'C38', b'C38'), (b'C39', b'C39')]),
        ),
        migrations.AlterField(
            model_name='nivel_3',
            name='sircunscripcion',
            field=models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34'), (b'C35', b'C35'), (b'C36', b'C36'), (b'C37', b'C37'), (b'C38', b'C38'), (b'C39', b'C39')]),
        ),
    ]
