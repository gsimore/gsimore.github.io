# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(default='Sub-Title', max_length=50)),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(choices=[('L', 'Landscape'), ('P', 'Portrait'), ('O', 'Other')], default='L', max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200)),
                ('height_in', models.IntegerField()),
                ('width_in', models.IntegerField()),
                ('description', models.TextField()),
                ('finish_date', models.DateField()),
                ('created', models.DateField()),
                ('thumbnail_image', models.ImageField(upload_to='')),
                ('small_image', models.ImageField(upload_to='')),
                ('large_image', models.ImageField(upload_to='')),
                ('draft', models.BooleanField(default=True)),
                ('image_rank', models.IntegerField()),
                ('collage_placement', models.PositiveIntegerField()),
                ('medium', models.CharField(choices=[('OL', 'Oil'), ('PC', 'Pencil'), ('IK', 'Ink'), ('WC', 'Watercolor'), ('DG', 'Digital'), ('MM', 'Mixed Media'), ('OT', 'Other')], default='OL', max_length=50)),
                ('pages', models.ManyToManyField(to='portfolio.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled', max_length=100)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_title', models.CharField(max_length=50)),
                ('show_description', models.TextField()),
                ('cover_photo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Piece')),
                ('show_pieces', models.ManyToManyField(related_name='shows', to='portfolio.Piece')),
            ],
        ),
    ]
