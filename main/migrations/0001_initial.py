# Generated by Django 5.0.7 on 2024-07-17 16:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='Series Slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('article_slug', models.CharField(max_length=200, unique=True, verbose_name='Article Slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date modified')),
                ('Series', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.articleseries', verbose_name='Series')),
            ],
        ),
    ]
