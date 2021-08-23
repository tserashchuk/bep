# Generated by Django 3.2.4 on 2021-08-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0032_auto_20210820_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-08-20 14:03:25.455731', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-08-20 14:03:25.389032', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-08-20 14:03:25.456488', max_length=200, verbose_name='URL'),
        ),
    ]
