# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nivel_2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('ci', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'nivel_2',
                'verbose_name_plural': 'nivel_2',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='control_electoral',
            options={'verbose_name': 'Control Electoral', 'verbose_name_plural': 'Control Electoral'},
        ),
        migrations.AddField(
            model_name='control_electoral',
            name='telefono',
            field=models.IntegerField(default='521'),
            preserve_default=False,
        ),
    ]
