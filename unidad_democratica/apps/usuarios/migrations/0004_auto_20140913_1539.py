# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20140910_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='nivel_3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('ci', models.IntegerField()),
                ('sircunscripcion', models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34')])),
                ('telefono', models.IntegerField()),
                ('lugar', models.CharField(max_length=100, choices=[(b'Urbano', b'Urbano'), (b'Rural', b'Rural')])),
            ],
            options={
                'verbose_name': 'Nivel 3',
                'verbose_name_plural': 'Nivel 3',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='control_electoral',
            name='sircunscripcion',
            field=models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34')]),
        ),
        migrations.AlterField(
            model_name='nivel_2',
            name='sircunscripcion',
            field=models.CharField(max_length=100, choices=[(b'C33', b'C33'), (b'C34', b'C34')]),
        ),
    ]
