# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_init', models.CharField(max_length=50, verbose_name='approval init')),
                ('approval_current', models.CharField(max_length=50, verbose_name='approval current')),
                ('commitments', models.CharField(max_length=50, verbose_name='commitments')),
                ('obligations', models.CharField(max_length=50, verbose_name='obligations')),
                ('payments', models.CharField(max_length=50, verbose_name='payments')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'investment',
                'verbose_name_plural': 'investment',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog', models.IntegerField(verbose_name='program')),
                ('subp', models.IntegerField(verbose_name='sub program')),
                ('proy', models.IntegerField(verbose_name='proyect')),
                ('subpr', models.IntegerField(verbose_name='sub proyect')),
                ('name', models.CharField(max_length=300, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'program',
                'verbose_name_plural': 'programs',
            },
        ),
        migrations.CreateModel(
            name='Rec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec', models.IntegerField(verbose_name='rec')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'rec',
                'verbose_name_plural': 'rec',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='code')),
                ('name', models.CharField(max_length=300, verbose_name='name')),
                ('unit', models.CharField(max_length=300, verbose_name='executing unit')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'sector',
                'verbose_name_plural': 'sectors',
            },
        ),
        migrations.CreateModel(
            name='Sit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sit', models.CharField(max_length=1, verbose_name='sit')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'sit',
                'verbose_name_plural': 'sit',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='source')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='year')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'year',
                'verbose_name_plural': 'years',
            },
        ),
        migrations.AddField(
            model_name='investment',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Program', verbose_name='program'),
        ),
        migrations.AddField(
            model_name='investment',
            name='rec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Rec', verbose_name='rec'),
        ),
        migrations.AddField(
            model_name='investment',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Sector', verbose_name='sector'),
        ),
        migrations.AddField(
            model_name='investment',
            name='sit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Sit', verbose_name='sit'),
        ),
        migrations.AddField(
            model_name='investment',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Source', verbose_name='source'),
        ),
        migrations.AddField(
            model_name='investment',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Year', verbose_name='year'),
        ),
    ]
