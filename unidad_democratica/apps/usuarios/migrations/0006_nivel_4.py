# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20140914_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='nivel_4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('ci', models.IntegerField()),
                ('sircunscripcion', models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34'), (b'C35', b'C35'), (b'C36', b'C36'), (b'C37', b'C37'), (b'C38', b'C38'), (b'C39', b'C39')])),
                ('telefono', models.IntegerField()),
                ('lugar', models.CharField(max_length=100, choices=[(b'Urbano', b'Urbano'), (b'Rural', b'Rural')])),
                ('municio_recinto', models.CharField(max_length=100)),
                ('mesa', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Nivel 4',
                'verbose_name_plural': 'Nivel 4',
            },
            bases=(models.Model,),
        ),
    ]
